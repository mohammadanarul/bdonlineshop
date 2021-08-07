from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .models import BuildingAddress
from payment.forms import CheckoutForm
from orders.models import Order

import stripe
stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"

class CheckoutView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        template_name = 'shop/checkout.html'
        return render(self.request, template_name, {'form': form})
    
    def post(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            form = CheckoutForm(self.request.POST or None)
            if form.is_valid():
                street_address = form.cleaned_data.get('street_address')
                living_address = form.cleaned_data.get('living_address')
                country = form.cleaned_data.get('country')
                post_code = form.cleaned_data.get('post_code')
                same_billing_address = form.cleaned_data.get('same_billing_address')
                save_info = form.cleaned_data.get('save_info')
                payment_option = form.cleaned_data.get('payment_option')
                building_address = BuildingAddress(
                    user = self.request.user,
                    street_address = street_address,
                    living_address = living_address,
                    country = country,
                    post_code = post_code,
                )
                building_address.save()
                order.building_address = building_address
                order.save()
                print(form.cleaned_data)
                print(building_address)
                messages.success(self.request, 'Your Order completed.')
                return redirect('/')
        except ObjectDoesNotExist:
            messages.info(self.request, 'Invalid Your Address.')
            return redirect('/')

class PaymentView(View):
    template_name = "payment/payment.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        stripe.Charge.create(
        amount=2000,
        currency="usd",
        source="tok_visa",
        description="My First Test Charge (created for API docs)",
        )

