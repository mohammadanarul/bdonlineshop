from django.urls import path
from orders.views import (
    OrderProductSummaryView,
    AddToCart,
    single_remove_cart,
    remove_from_cart,
)

app_name = 'orders'
urlpatterns = [
    path('order-summary/', OrderProductSummaryView.as_view(), name='order_summary'),
    path('add-to-cart/<slug>/', AddToCart.as_view(), name='add_to_cart'),
    path('single-item-remove-from-cart/<slug>/', single_remove_cart, name='single_item_remove'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove_from_cart'),
]