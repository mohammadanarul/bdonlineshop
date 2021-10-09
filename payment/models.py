from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField

from payment.forms import PAYMENT_CHOICES

User = settings.AUTH_USER_MODEL

ADDRESS_CHOICES = (
    ('Billing', 'Billing'),
    ('Shipping', 'Shipping'),
)
class Address(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip_code = models.CharField(max_length=100)
    address_type = models.CharField(max_length=10, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username}/{self.address_type}/{self.default}'

    class Meta:
        verbose_name_plural = 'Addresses'

class Payment(models.Model):
    payment_charge_id        =   models.CharField(max_length=50)
    user                    =   models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
    payment_option          = models.CharField(max_length=50, default='Cash on Delivery', choices=PAYMENT_CHOICES)
    amount                  =   models.FloatField(_("amount"))
    timestamp               =   models.DateTimeField(_("timestamp"), auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return f'{self.user} -> {self.payment_option}'
    
