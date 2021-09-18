from django.db import models
from shop.models import Product
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from payment.models import Address, Payment
User = settings.AUTH_USER_MODEL

class OrderItemManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        order_item = super(OrderItemManager, self).get_queryset(*args, **kwargs).filter(ordered=True)
        return order_item

class OrderItem(models.Model):
    user                  =   models.ForeignKey(User, on_delete=models.CASCADE)
    item                  =   models.ForeignKey(Product, related_name='order_item', on_delete=models.SET_NULL, null=True)
    quantity              =   models.IntegerField(default=1)
    ordered               =   models.BooleanField(default=False)
    date_added            =   models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    order_item_manager = OrderItemManager()

    def get_total_quantity(self):
        return self.quantity 

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
    
    def __str__(self):
        return f'{self.quantity} of {self.item.title} | {self.user}'
    



class Order(models.Model):
    user                  =   models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
    items                 =   models.ManyToManyField(OrderItem, verbose_name=_("items"))
    start_date            =   models.DateTimeField(auto_now_add=True, verbose_name=_("start date"))
    ordered_date          =   models.DateTimeField(verbose_name=_("ordered date"))
    ordered               =   models.BooleanField(default=False, verbose_name=_("ordered"))
    shipping_address      = models.ForeignKey(
        Address, related_name='shipping_address',
        on_delete=models.SET_NULL, blank=True, null=True)
    billing_address       = models.ForeignKey(
        Address, related_name='billing_address',
        on_delete=models.SET_NULL, blank=True, null=True)
    payment               =   models.ForeignKey(Payment, verbose_name=_("payment"), on_delete=models.SET_NULL, blank=True, null=True)

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