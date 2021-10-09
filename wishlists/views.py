from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView, DeleteView
from django.contrib import messages
from shop.models import Product
from .models import Wishlist

class WishListView(LoginRequiredMixin, View):
    template_name = 'wish-lists.html'
    def get(self, request, *args, **kwargs):
        wishlist = Wishlist.objects.filter(user=request.user)
        return render(request, self.template_name, {'object_list': wishlist})
        
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

class SingeWishListDeleteView(LoginRequiredMixin, DeleteView):
    # specify the model you want to use
    model = Wishlist
     
    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url = '/wishlist/list/'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != self.request.user:
            return redirect(self.success_url)
        return super().post(request, *args, **kwargs)
