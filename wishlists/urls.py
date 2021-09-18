from django.urls import path
from .views import WishListAddView

app_name = 'wishlists'
urlpatterns = [
    path('add/<slug>/', WishListAddView.as_view(), name='wishlist_add_view'),
]
