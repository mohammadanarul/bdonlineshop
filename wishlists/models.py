from django.db import models
from django.conf import settings
from shop.models import Product
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='wishlist' , on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product.title
    
    def total_wishlist(self):
        total = 0
        for qs in self.product.all():
            total += qs
        return total
