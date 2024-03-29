from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Size(models.Model):
    name = models.CharField(_("name"), max_length=50)
    code = models.CharField(_("code"), max_length=50)

    def __str__(self):
        return self.name
    