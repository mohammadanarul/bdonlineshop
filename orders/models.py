from django.db import models
from shop.models import Product
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from payment.models import BuildingAddress
User = settings.AUTH_USER_MODEL

class OrderItem(models.Model):
    user                  =   models.ForeignKey(User, on_delete=models.CASCADE)
    item                  =   models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity              =   models.IntegerField(default=1)
    ordered               =   models.BooleanField(default=False)

    def get_total_item_price(self):
        return self.item.price * self.quantity
    
    def get_total_item_discount_price(self):
        return self.item.discount_price * self.quantity
    
    def get_item_final_ammount(self):
        return self.get_total_item_price() - self.get_total_item_discount_price()
    
    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_item_discount_price()
        return self.get_total_item_price()



class Order(models.Model):
    user                  =   models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
    items                 =   models.ManyToManyField(OrderItem, verbose_name=_("items"))
    start_date            =   models.DateTimeField(auto_now_add=True, verbose_name=_("start date"))
    ordered_date          =   models.DateTimeField(verbose_name=_("ordered date"))
    ordered               =   models.BooleanField(default=False, verbose_name=_("building address"))
    building_address      =   models.ForeignKey(BuildingAddress, verbose_name=_("building address"), on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.user}-{self.pk}"
    
    def get_total_price(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_item_final_ammount()
        return total

    def get_save_ammount(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total