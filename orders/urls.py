from django.urls import path
from orders.views import (
    order_summary_view,
    add_to_cart,
    single_remove_cart,
)

app_name = 'orders'
urlpatterns = [
    path('order-summary/', order_summary_view.as_view(), name='order_summary'),
    path('add-to-cart/<slug>/', add_to_cart, name='add_to_cart'),
    path('single-item-remove-from-cart/<slug>/', single_remove_cart, name='single_item_remove'),
]

# 02255105
# mnbvcxzlkj21