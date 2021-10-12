from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from blog.views import about as about_view
# from django.conf.urls import (
#     handler400,
#     handler403,
#     handler404,
#     handler500
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls', namespace='account')),
    path('', include('shop.urls', namespace='shop')),
    path('category/', include('category.urls', namespace='category')),
    path('order/', include('orders.urls', namespace='order')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('wishlist/', include('wishlists.urls', namespace='wishlist')),
    path('auth', include('django.contrib.auth.urls')),
    # about 
    path('about/', about_view, name='about_page'),
]

# error handling path
handler400 = 'blog.views.bad_request'
handler403 = 'blog.views.permission_denied'
handler404 = 'blog.views.page_not_found'
handler500 = 'blog.views.server_error'

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
