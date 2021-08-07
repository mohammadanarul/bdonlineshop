from django.urls import path
from shop.views import (
    HomeView,
    ShopProductView,
    SingleProductView
)

app_name = 'shop'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop/', ShopProductView.as_view(), name='shop_view'),
    path('single-product/<slug>/', SingleProductView.as_view(), name='single_shop_view'),
]
