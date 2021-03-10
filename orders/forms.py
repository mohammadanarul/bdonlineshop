from django import forms
from django_countries.fields import CountryField

PAYMENT_CHOICES = (
    ('s', 'Stripe'),
    ('b', 'Bkash'),
    ('n', 'Nagot'),
)

class CheckoutForm(forms.Form):
    street_address = forms.CharField()
    living_address = forms.CharField()
    country = CountryField()
    post_code = forms.CharField()
    same_billing_address = forms.BooleanField()
    save_info = forms.BooleanField()
    payment_option - forms.ChoiceField(choices=PAYMENT_CHOICES)
