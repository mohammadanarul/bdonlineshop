from django import forms
from django_countries.fields import CountryField

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('B', 'Bkash'),
    ('N', 'Nagot'),
)

class CheckoutForm(forms.Form):
    street_address = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-2'}))
    living_address = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-2'})
    )
    country = CountryField(blank_label='(select country)').formfield()
    post_code = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-2'})
    )
    same_billing_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(choices=PAYMENT_CHOICES)