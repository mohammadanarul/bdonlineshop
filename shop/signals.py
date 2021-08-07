from django.db.models.signals import post_save, pre_save
from django.utils.text import slugify
from django.dispatch import receiver
from shop.models import Product

@receiver(post_save, sender=Product)
def shop_product_save(sender, instance, created, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        instance.save()

@receiver(pre_save, sender=Product)
def shop_product_save(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)