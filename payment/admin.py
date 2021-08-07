from django.contrib import admin
from .models import BuildingAddress

@admin.register(BuildingAddress)
class BuildingAddressAdminModel(admin.ModelAdmin):
    pass
