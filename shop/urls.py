from django.urls import path
from shop.views import (
    HomeView,
    shop_page_view,
    single_shop_view
)

app_name = 'shop'
urlpatterns = [
    path('', HomeView, name='home'),
    path('shop/', shop_page_view, name='shop_view'),
    path('<slug>/', single_shop_view, name='single_shop_view'),
]
