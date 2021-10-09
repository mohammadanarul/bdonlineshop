from django.urls import path
from account.views import (
    UserLoginView,
    UserLogoutView,
    DashboardView,
    UserRegisterView,
    UserAccountActivateView,
    PasswordResetView,
)

app_name = 'account'
urlpatterns = [
    path('user-register/', UserRegisterView.as_view(), name='user_register'),
    path('activate/<uid>/<token>', UserAccountActivateView.as_view(), name='activate_view'),
    path('user-login/', UserLoginView.as_view(), name='user_login'),
    path('user-logout/', UserLogoutView.as_view(), name='user_logout'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset_view'),
    path('dashboard/<username>/', DashboardView.as_view(), name='user_dashboard'),
]
