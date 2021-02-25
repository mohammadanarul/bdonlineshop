from django.shortcuts import render, get_object_or_404
from category.models import Category
from shop.models import Product

def category_list_page_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    objects = Product.objects.filter(category=category)
    template_name = 'category/category-list.html'
    return render(request, template_name, {'objects': objects})