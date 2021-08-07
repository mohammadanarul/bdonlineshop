from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, DetailView
from shop.models import Product
from category.models import Category
from brands.models import Brand
from colors.models import Color
from sizes.models import Size

class HomeView(ListView):
    model = Product
    template_name = 'shop/home.html'

class ShopProductView(View):
    template_name = 'shop/shop.html'
    def get(self, request, *args, **kwargs):
        product = Product.objects.all()
        category = Category.objects.all()
        brand = Brand.objects.all()
        color = Color.objects.all()
        size = Size.objects.all()
        context = {
            'product': product,
            'category': category,
            'brands': brand,
            'colors': color,
            'sizes': size
        }
        return render(request, self.template_name, context)

class SingleProductView(DetailView):
    model = Product
    template_name = 'shop/product-details.html'

