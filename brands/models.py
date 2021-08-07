from django.db import models
from django.utils.translation import ugettext_lazy as _

class Brand(models.Model):
    brand_name = models.CharField(_("brand name"), max_length=50)

    def __str__(self):
        return self.brand_name
    
