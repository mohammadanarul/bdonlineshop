from django.shortcuts import render
from shop.models import Product

def HomeView(request):
    template_name = 'shop/home.html'
    return render(request, template_name)

def shop_page_view(request):
    obj = Product.objects.all()
    template_name = 'shop/shop.html'
    return render(request, template_name, {'objects': obj})
