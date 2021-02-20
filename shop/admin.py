from django.contrib import admin
from shop.models import Product, ProductImages


class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 1

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInline]
