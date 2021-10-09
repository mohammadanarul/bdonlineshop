from django.urls import path
from .views import WishListAddView, WishListView, SingeWishListDeleteView

app_name = 'wishlists'
urlpatterns = [
    path('list/', WishListView.as_view(), name='wishlist_lists'),
    path('add/<slug>/', WishListAddView.as_view(), name='wishlist_add_view'),
    path('delete/<pk>/', SingeWishListDeleteView.as_view(), name='wishlist_delete_view'),
]
