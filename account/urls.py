from django.urls import path
from account.views import (
    user_register_page,
    user_login_page,
    user_logout_page
)

app_name = 'account'
urlpatterns = [
    path('user-register/', user_register_page, name='user_register'),
    path('user-login/', user_login_page, name='user_login'),
    path('user-logout/', user_logout_page, name='user_logout'),
]
