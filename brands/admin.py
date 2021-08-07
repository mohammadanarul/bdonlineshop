from django.contrib import admin
from .models import Brand

@admin.register(Brand)
class BrandModelAdmin(admin.ModelAdmin):
    pass
