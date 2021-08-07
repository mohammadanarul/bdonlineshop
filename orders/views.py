from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.utils import timezone
from django.contrib import messages
from shop.models import Product
from orders.models import Order, OrderItem

class OrderProductSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            template_name = 'shop/cart.html'
            return render(self.request, template_name, {'orders': order})
        except ObjectDoesNotExist:
            messages.info(self.request, 'You do not have an active  order.')
            next = self.request.META['HTTP_REFERER']
            return HttpResponseRedirect(next)
class AddToCart(LoginRequiredMixin, View):
    def get(self, request, slug, *args, **kwargs):
        item = get_object_or_404(Product, slug=slug)
        order_item, created = OrderItem.objects.get_or_create(
            item=item,
            user=request.user,
            ordered=False
        )
        order_qs = Order.objects.filter(
            user=request.user,
            ordered=False
        )
        next = self.request.META['HTTP_REFERER']
        if order_qs.exists():
            order = order_qs[0]
            # check if the order item is in the order
            if order.items.filter(item__slug=item.slug).exists():
                order_item.quantity += 1
                order_item.save()
                messages.info(request, 'This item quantity was updated.')
                return HttpResponseRedirect(next)
            else:
                order.items.add(order_item)
                messages.info(request, 'This item was added to your cart.')
                return HttpResponseRedirect(next)
        else:
            ordered_date = timezone.now()
            order = Order.objects.create(
                user=request.user,
                ordered_date=ordered_date
            )
            order.items.add(order_item)
            messages.info(request, 'This item was added to your cart.')
            return HttpResponseRedirect(next)

def single_remove_cart(request, slug):
    item = get_object_or_404(
    Product,
    slug=slug
    )
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, 'Single item remove from cart.')
            return redirect('order:order_summary')
        else:
            messages.info(request, 'This item was not in your cart.')
            return redirect('order:order_summary')
    else:
        messages.info(request, 'You do not have an active  order.')
        return redirect('shop:shop_view')

# item remove from cart.
def remove_from_cart(request, slug):
    item = get_object_or_404(
        Product,
        slug=slug
    )
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, 'This item was removed from your cart.')
            return redirect('shop:shop_view')
        else:
            messages.info(request, 'This item was not in your catd.')
            return redirect('shop:shop_view')
    else:
        messages.info(request, 'You do not have an active order.')
        return redirect('shop:shop_view')

    


