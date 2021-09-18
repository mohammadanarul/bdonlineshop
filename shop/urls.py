from django.urls import path
from shop.views import (
    HomeView,
    ShopProductView,
    SingleProductView,
    WishlistAddView,
    ReviewRatingCreateView,
)

app_name = 'shop'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop/', ShopProductView.as_view(), name='shop_view'),
    path('single-product/<slug>/', SingleProductView.as_view(), name='single_shop_view'),
    path('add/<slug>/', WishlistAddView.as_view(), name='add_wishlist_view'),
    path('review-rating-add/<product_id>/', ReviewRatingCreateView.as_view(), name='review_ratting_view'),
]
