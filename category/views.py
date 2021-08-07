from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import View
from category.models import Category
from shop.models import Product

class CategoryListPageView(View):
    template_name = 'category/category-list.html'
    def get(self, request, slug):
        category = get_object_or_404(Category)
        objects = Product.objects.filter(category=category)
        return render(request, self.template_name, {'objects': objects})