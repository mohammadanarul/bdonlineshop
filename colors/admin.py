from django.contrib import admin
from .models import Color
# Register your models here.

@admin.register(Color)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ('color_name', 'color_tag')
