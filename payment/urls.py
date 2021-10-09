from django.urls import path
from payment.views import (
    CheckoutView,
    StripePaymentView,
    PapalPaymentView,
    SSLCommerzPaymentView,
)

app_name = 'payment'
urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout_view'),
    path('stripe/<payment_option>/', StripePaymentView.as_view(), name='stripe_payment_view'),
    path('paypal/<payment_option>/', PapalPaymentView.as_view(), name='paypal_payment_view'),
    path('sslcommerz/<payment_option>/', SSLCommerzPaymentView.as_view(), name='sslcommerz_payment_view'),
]