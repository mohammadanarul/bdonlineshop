from django.urls import path
from shop.views import (
    HomeView
)

app_name = 'shop'
urlpatterns = [
    path('', HomeView, name='home'),
]
