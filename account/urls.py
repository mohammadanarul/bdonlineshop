from django.urls import path
from account.views import (
    user_register_page,
)

app_name = 'account'
urlpatterns = [
    path('user-register/', user_register_page, name='user-register'),
]
