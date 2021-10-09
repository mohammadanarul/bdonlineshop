from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .models import Address, Payment
from payment.forms import CheckoutForm
from orders.models import Order
from account.models import Account

import stripe
stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"


def is_valid_form(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid
class CheckoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            order = Order.objects.get(user=request.user, ordered=False)
            form = CheckoutForm()
            context = {
                'form': form,
                'order': order
            }
            shipping_address_qs = Address.objects.filter(
                user=request.user,
                address_type = "Shipping",
                default=True
            )
            if shipping_address_qs.exists():
                context.update(
                    {'default_shipping_address': shipping_address_qs[0]}
                )
            billing_address_qs = Address.objects.filter(
                user=request.user,
                address_type= 'Billing',
                default=True
            )
            if billing_address_qs.exists():
                context.update(
                    {'default_billing_address': billing_address_qs[0]}
                )
            template_name = 'shop/checkout.html'
            return render(self.request, template_name, context)
        except ObjectDoesNotExist:
            messages.info(request, 'You do not have an active  order.')
            return redirect('payment:checkout_view')
    
    def post(self, request, *args, **kwargs):
        try:
            order = Order.objects.get(user=request.user, ordered=False)
            form = CheckoutForm(request.POST or None)
            if form.is_valid():
                use_default_shipping = form.cleaned_data.get('use_default_shipping')
                if use_default_shipping:
                    address_qs = Address.objects.filter(
                        user=request.user,
                        address_type="Shipping",
                        default=True
                    )
                    if address_qs.exists():
                        shipping_address = address_qs[0]
                        order.shipping_address = shipping_address
                        order.save()
                    else:
                        messages.info(request,"No Default shipping address available")
                        return redirect('payment:checkout_view')
                else:
                    shipping_address1 = form.cleaned_data.get('shipping_address')
                    shipping_address2 = form.cleaned_data.get('shipping_address2')
                    shipping_country = form.cleaned_data.get('shipping_country')
                    shipping_zip = form.cleaned_data.get('shipping_zip')
                    if is_valid_form([shipping_address1, shipping_country, shipping_zip]):
                        shipping_address = Address(
                            user=request.user,
                            street_address = shipping_address1,
                            apartment_address = shipping_address2 ,
                            country = shipping_country,
                            zip_code = shipping_zip,
                            address_type = 'Shipping'
                        )
                        shipping_address.save()
                        order.shipping_address = shipping_address
                        order.save()
                        set_default_shipping = form.cleaned_data.get('set_default_shipping')
                        if set_default_shipping:
                            shipping_address.default = True
                            shipping_address.save()
                    else:
                        messages.info(request, 'Kindly fill in the required shipping address form.')

                use_default_billing = form.cleaned_data.get('use_default_billing')
                same_billing_address = form.cleaned_data.get('same_billing_address')
                if same_billing_address:
                    billing_address = shipping_address
                    billing_address.pk = None
                    billing_address.save()
                    billing_address.address_type = 'Billing'
                    billing_address.save()
                    order.billing_address = billing_address
                    order.save()
                elif use_default_billing:
                    address_qs = Address.objects.filter(
                        user=request.user,
                        address_type= "Billing",
                        default=True
                    )
                    if address_qs.exists():
                        billing_address = address_qs[0]
                        order.billing_address = billing_address
                        order.save()
                    else:
                        messages.info(request, 'No default billing address available.')
                        return redirect('payment:checkout_view')
                else:
                    billing_address1 = form.cleaned_data.get('billing_address')
                    billing_address2 = form.cleaned_data.get('billing_address2')
                    billing_country = form.cleaned_data.get('billing_country')
                    billing_zip = form.cleaned_data.get('billing_zip')

                    if is_valid_form([billing_address1, billing_country, billing_zip]):
                        billing_address = Address(
                            user=request.user,
                            street_address= shipping_address1,
                            apartment_address= shipping_address2,
                            country=billing_country,
                            zip_code=billing_zip,
                            address_type="Billing"
                        )
                        billing_address.save()
                        order.billing_address = billing_address
                        order.save()
                        set_default_billing = form.cleaned_data.get('set_default_billing')
                        if set_default_billing:
                            billing_address.default = True
                            billing_address.save()
                    else:
                        messages.info(request, 'Please fill in the required billing address form')
                payment_option = form.cleaned_data.get('payment_option')
                if payment_option == 'Cash on Delivery':
                    order = Order.objects.get(user=request.user, ordered=False)
                    payment = Payment()
                    payment.stripe_charge_id = order.id
                    payment.user = request.user
                    payment.amount = order.get_total_price()
                    payment.save()

                    # assign the payment to the order
                    order_items = order.items.all()
                    for item in order_items:
                        item.ordered = True
                        item.save()
                    order.ordered = True
                    order.payment = payment
                    order.save()
                    messages.success(self.request, "Your order was successful!")
                    return redirect("/")
                if payment_option == 'Stripe':
                    return redirect('payment:stripe_payment_view', payment_option='stripe')
                elif payment_option == 'PayPal':
                    return redirect('payment:paypal_payment_view', payment_option='paypal')
                    messages.info(request, 'Not Active paypal services...')
                elif payment_option == 'sslcommerz':
                    return redirect('payment:sslcommerz_payment_view', payment_option='sslcommerz')
                    messages.info(request, 'Not Active sslcommerz services...')
                else:
                    messages.warning(request, 'Invalid payment option selected.')
                    return redirect('payment:checkout_view')
                messages.success(self.request, 'Your Order completed.')
            else:
                form = CheckoutForm(request)
        except ObjectDoesNotExist:
            messages.info(self.request, 'Invalid Your Address.')
            return redirect('/')

class StripePaymentView(View):
    template_name = "payment/stripe.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        order = Order.objects.get(user=request.user, ordered=False)
        token = request.POST.get('stripeToken')
        # userprofile = Account.objects.get(user=self.request.user)
        # if form.is_valid():
        #     token = form.cleaned_data.get('stripeToken')
        #     save = form.cleaned_data.get('save')
        #     use_default = form.cleaned_data.get('use_default')

        #     if save:
        #         if userprofile.stripe_customer_id != '' and userprofile.stripe_customer_id is not None:
        #             customer = stripe.Customer.retrieve(
        #                 userprofile.stripe_customer_id)
        #             customer.sources.create(source=token)

        #         else:
        #             User = stripe.Customer.create(
        #                 email=self.request.user.email,
        #             )
        #             customer.sources.create(source=token)
        #             userprofile.stripe_customer_id = customer['id']
        #             userprofile.one_click_purchasing = True
        #             userprofile.save()
        amount = int(order.get_total_price() * 100)
        try:
            # charge once off on the token
            charge = stripe.Charge.create(
            amount=amount, #cents
            currency="usd",
            source=token,
            )
            # create the payment
            payment = Payment()
            payment.stripe_charge_id = charge['id']
            payment.user = request.user
            payment.amount = amount
            payment.save()

            # assign the payment to the order
            order_items = order.items.all()
            for item in order_items:
                item.ordered = True
                item.save()
            order.ordered = True
            order.payment = payment
            order.save()
            messages.success(self.request, "Your order was successful!")
            return redirect("/")
        except stripe.error.CardError as e:
                body = e.json_body
                err = body.get('error', {})
                messages.warning(self.request, f"{err.get('message')}")
                return redirect("/")

        except stripe.error.RateLimitError as e:
            # Too many requests made to the API too quickly
            messages.warning(self.request, "Rate limit error")
            return redirect("/")

        except stripe.error.InvalidRequestError as e:
            # Invalid parameters were supplied to Stripe's API
            print(e)
            messages.warning(self.request, "Invalid parameters")
            return redirect("/")

        except stripe.error.AuthenticationError as e:
            # Authentication with Stripe's API failed
            # (maybe you changed API keys recently)
            messages.warning(self.request, "Not authenticated")
            return redirect("/")

        except stripe.error.APIConnectionError as e:
            # Network communication with Stripe failed
            messages.warning(self.request, "Network error")
            return redirect("/")

        except stripe.error.StripeError as e:
            # Display a very generic error to the user, and maybe send
            # yourself an email
            messages.warning(
                self.request, "Something went wrong. You were not charged. Please try again.")
            return redirect("/")

        except Exception as e:
            # send an email to ourselves
            messages.warning(
                self.request, "A serious error occurred. We have been notifed.")
            return redirect("/")

class PapalPaymentView(View):
    template_name = "payment/paypal.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        order = Order.objects.get(user=request.user, ordered=False)
        token = request.POST.get('stripeToken')
        # userprofile = Account.objects.get(user=self.request.user)
        # if form.is_valid():
        #     token = form.cleaned_data.get('stripeToken')
        #     save = form.cleaned_data.get('save')
        #     use_default = form.cleaned_data.get('use_default')

        #     if save:
        #         if userprofile.stripe_customer_id != '' and userprofile.stripe_customer_id is not None:
        #             customer = stripe.Customer.retrieve(
        #                 userprofile.stripe_customer_id)
        #             customer.sources.create(source=token)

        #         else:
        #             User = stripe.Customer.create(
        #                 email=self.request.user.email,
        #             )
        #             customer.sources.create(source=token)
        #             userprofile.stripe_customer_id = customer['id']
        #             userprofile.one_click_purchasing = True
        #             userprofile.save()
        amount = int(order.get_total_price() * 100)
        # charge once off on the token
        charge = stripe.Charge.create(
        amount=amount, #cents
        currency="usd",
        source=token,
        )
        # create the payment
        payment = Payment()
        payment.stripe_charge_id = charge['id']
        payment.user = request.user
        payment.amount = amount
        payment.save()

        # assign the payment to the order
        order_items = order.items.all()
        for item in order_items:
            item.ordered = True
            item.save()
        order.ordered = True
        order.payment = payment
        order.save()
        messages.success(self.request, "Your order was successful!")
        return redirect("/")
        

class SSLCommerzPaymentView(View):
    template_name = "payment/payment.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        order = Order.objects.get(user=request.user, ordered=False)
        token = request.POST.get('stripeToken')
        # userprofile = Account.objects.get(user=self.request.user)
        # if form.is_valid():
        #     token = form.cleaned_data.get('stripeToken')
        #     save = form.cleaned_data.get('save')
        #     use_default = form.cleaned_data.get('use_default')

        #     if save:
        #         if userprofile.stripe_customer_id != '' and userprofile.stripe_customer_id is not None:
        #             customer = stripe.Customer.retrieve(
        #                 userprofile.stripe_customer_id)
        #             customer.sources.create(source=token)

        #         else:
        #             User = stripe.Customer.create(
        #                 email=self.request.user.email,
        #             )
        #             customer.sources.create(source=token)
        #             userprofile.stripe_customer_id = customer['id']
        #             userprofile.one_click_purchasing = True
        #             userprofile.save()
        amount = int(order.get_total_price() * 100)
            # charge once off on the token
        charge = stripe.Charge.create(
        amount=amount, #cents
        currency="usd",
        source=token,
        )
        # create the payment
        payment = Payment()
        payment.stripe_charge_id = charge['id']
        payment.user = request.user
        payment.amount = amount
        payment.save()

        # assign the payment to the order
        order_items = order.items.all()
        for item in order_items:
            item.ordered = True
            item.save()
        order.ordered = True
        order.payment = payment
        order.save()
        messages.success(self.request, "Your order was successful!")
        return redirect("/")


