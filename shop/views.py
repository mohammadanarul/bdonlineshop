from django.db.models import F, Count, Sum
from datetime import datetime, timedelta
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from shop.models import Product, ReviewRating
from category.models import Category
from brands.models import Brand
from colors.models import Color
from sizes.models import Size
from datetime import datetime
from django.contrib import messages
from .forms import ReviewRatingForm

class HomeView(ListView):
    model = Product
    template_name = 'shop/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update({
            'featured_product': Product.objects.filter(is_featured=True),
            'on_sale_product': Product.objects.filter(on_sale=True),
            'popular_category': Category.objects.annotate(num_product=Count('products')).order_by('-num_product')[:12],
            'top_selling_product': Product.objects.filter(
                order_item__date_added__lte=datetime.today(),
                order_item__date_added__gt=datetime.today()-timedelta(days=7),
                order_item__ordered=True
            ).annotate(quantity_sum=Sum('order_item__quantity')).order_by('-quantity_sum')[:10]
        })
        return context

class ShopProductView(ListView):
    template_name = 'shop/shop.html'
    model = Product

class SingleProductView(DetailView):
    model = Product
    template_name = 'shop/product.html'

    def get_object(self):
        obj = super(SingleProductView, self).get_object()
        obj.last_view = datetime.now()
        obj.save()
        return obj
    
    def get_context_data(self, **kwargs):
        context = super(SingleProductView, self).get_context_data(**kwargs)
        product_id = self.request.POST.get('product_id')
        context.update({
            'product_reviews': ReviewRating.objects.filter(product_id=product_id, status=True)
        })
        return context 

class WishlistView(LoginRequiredMixin, View):
    template_name = 'post/favorite-list.html'

        
class WishlistAddView(LoginRequiredMixin, View):
    def get(self, request, slug):
        product = Product.objects.get(slug=slug)
        if product.wished.filter(id=request.user.pk).exists():
            product.wished.remove(request.user)
        else:
            product.wished.add(request.user)
        next = request.META['HTTP_REFERER']
        return HttpResponseRedirect(next)

class ReviewRatingCreateView(LoginRequiredMixin, View):
    ''' Review ratting add function'''
    def post(self, request, product_id):
        if request.method == 'POST':
            url = request.META.get('HTTP_REFERER')
            try:
                review = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
                form = ReviewRatingForm(request.POST or None, instance=review)
                form.save()
                messages.warning(request, 'Thank you! your review has been updated.')
                return HttpResponseRedirect(url)
            except ReviewRating.DoesNotExist:
                form = ReviewRatingForm(request.POST or None)
                if form.is_valid():
                    data = form.save(commit=False)
                    data.product_id = product_id
                    data.user_id = request.user.id
                    data.ip = request.META.get('REMOTE_ADDR')
                    data.last_review = datetime.now()
                    data.save()
                    messages.success(request, "Thank you! Your review has been submitted.")
                    return HttpResponseRedirect(url)
                    



