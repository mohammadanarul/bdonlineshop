from django.contrib import admin
from .models import Size

@admin.register(Size)
class SizeModelAdmin(admin.ModelAdmin):
    pass
