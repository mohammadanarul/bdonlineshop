from django.contrib import admin
from shop.models import Product, ProductImages, ReviewRating
from variants.models import ProductVariant

class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    readonly_fields = ('id',)
    extra = 1

class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInline, ProductVariantInline]

admin.site.register(ReviewRating)
