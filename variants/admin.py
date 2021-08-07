from django.contrib import admin
from .models import ProductVariant

@admin.register(ProductVariant)
class ProductVariantModelAdmin(admin.ModelAdmin):
    pass
