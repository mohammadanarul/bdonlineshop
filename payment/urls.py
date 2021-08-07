from django.urls import path
from payment.views import (
    CheckoutView,
    PaymentView
)

app_name = 'payment'
urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout_view'),
    path('payment/', PaymentView.as_view(), name='payment_view'),
]