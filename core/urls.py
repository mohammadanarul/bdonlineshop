from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from blog.views import about as about_view
from django.contrib.auth import views as auth_views

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
    
    # password reset url configaration
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'), name='password_reset_complete'),
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
