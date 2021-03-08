from django.shortcuts import render, get_object_or_404
from shop.models import Product
from category.models import Category

def HomeView(request):
    product = Product.objects.all()
    category = Category.objects.all()
    template_name = 'shop/home.html'
    context = {
        'category': category,
        'product': product,
    }
    return render(request, template_name, context)

def shop_page_view(request):
    category = Category.objects.all()
    product = Product.objects.all()
    template_name = 'shop/shop.html'
    return render(request, template_name, {'product': product, 'category': category,})

def single_shop_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    template_name = 'shop/product-details.html'
    return render(request, template_name, {'product': product})

