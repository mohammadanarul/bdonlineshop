from django.contrib import admin
from .models import Address, Payment

@admin.register(Address)
class AddressAdminModel(admin.ModelAdmin):
    list_display = ('user', 'street_address', 'apartment_address', 'country', 'zip_code', 'address_type', 'default')


admin.site.register(Payment)