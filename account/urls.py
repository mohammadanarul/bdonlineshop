from django.urls import path
from account.views import (
    user_register_page,
    user_login_page,
    user_logout_page,
    user_dashboard_page_view
)

app_name = 'account'
urlpatterns = [
    path('user-register/', user_register_page, name='user_register'),
    path('user-login/', user_login_page, name='user_login'),
    path('user-logout/', user_logout_page, name='user_logout'),
    path('@<str:username>/', user_dashboard_page_view, name='user_dashboard'),
]
