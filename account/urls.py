from django.urls import path
from account.views import (
    UserRegisterView,
    UserLoginView,
    UserLogoutView,
    user_dashboard_page_view
)

app_name = 'account'
urlpatterns = [
    path('user-register/', UserRegisterView.as_view(), name='user_register'),
    path('user-login/', UserLoginView.as_view(), name='user_login'),
    path('user-logout/', UserLogoutView.as_view(), name='user_logout'),
    path('@<str:username>/', user_dashboard_page_view, name='user_dashboard'),
]
