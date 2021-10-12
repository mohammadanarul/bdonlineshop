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
    path('dashboard/<username>/', DashboardView.as_view(), name='user_dashboard'),
    
    # password reset url configaration
    path('password-reset/', PasswordResetView.as_view(), name='password_reset_view'),
]


# password reset
'''
path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
'''