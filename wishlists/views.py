from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView
from django.contrib import messages
from shop.models import Product
from .models import Wishlist

class WishListView(LoginRequiredMixin, View):
    template_name = 'post/favorite-list.html'
    def get(self, request, *args, **kwargs):
        wishlist = Product.objects.filter(wishlist=request.user)
        return render(request, self.template_name, {'wishlist_list': favorite})
        
class WishListAddView(LoginRequiredMixin, View):
    def get(self, request, slug):
        user = request.user
        product = Product.objects.get(slug=slug)
        if Wishlist.objects.filter(product_id=product.id).exists():
            messages.info(request, 'Already added your wishlist cart.')
        else:
            wishlist = Wishlist.objects.create(
                user=user,
                product=product
            )
            wishlist.save()
        next = request.META['HTTP_REFERER']
        return HttpResponseRedirect(next)
