from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField

User = settings.AUTH_USER_MODEL

class BuildingAddress(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
    street_address = models.CharField(max_length=250)
    living_address = models.CharField(max_length=250)
    country = CountryField(multiple=False)
    post_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user}/{self.country}/{self.post_code}"
    
