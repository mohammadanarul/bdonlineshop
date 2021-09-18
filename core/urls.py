from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls', namespace='account')),
    path('', include('shop.urls', namespace='shop')),
    path('category/', include('category.urls', namespace='category')),
    path('order/', include('orders.urls', namespace='order')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('wishlist/', include('wishlists.urls', namespace='wishlist')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
