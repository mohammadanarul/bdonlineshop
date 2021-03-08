from django.contrib import admin
from orders.models import Order, OrderItem


@admin.register(OrderItem)
class OrderItemModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'quantity', 'get_item_final_ammount', 'ordered')

@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    pass
