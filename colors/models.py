from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

class Color(models.Model):
    color_name = models.CharField(_("color name"), max_length=50)
    code = models.CharField(_("code"), max_length=50)

    def __str__(self):
        return self.color_name
    
    def color_tag(self):
        if self.code is not None:
            return mark_safe('<p style="background-color:{}">Color</p>'.format(self.code))
        else:
            return ''   
    
