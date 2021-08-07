from django.db import models
from django.utils.translation import ugettext_lazy as _
from shop.models import Product, ProductImages
from colors.models import Color
from sizes.models import Size


class ProductVariant(models.Model):
    title               =   models.CharField(max_length=255, verbose_name=_("title"), blank=True, null=True)
    product             =   models.ForeignKey(Product, verbose_name=_("product"), on_delete=models.CASCADE)
    color               =   models.ForeignKey(Color, verbose_name=_("color"), on_delete=models.CASCADE, blank=True, null=True)
    size                =   models.ForeignKey(Size, verbose_name=_("size"), on_delete=models.CASCADE, blank=True, null=True)
    image_id            =   models.IntegerField(_("image id"), blank=True, null=True)
    price               =   models.FloatField(default=1, verbose_name=_("price"), blank=True, null=True)
    quantity            =   models.IntegerField(default=1)

    def __str__(self):
        if self.title is not None:
            return self.title
        else:
            return ''
    

    def image(self):
        img = ProductImages.objects.get(id=self.image_id)
        if img.id is not None:
            variant_product_image = img.images.url
        else:
            variant_product_image = ''
        return variant_product_image
    
    def image_tag(self):
        img = ProductImages.objects.get(id=self.image_id)
        if img.id is not None:
            return mark_safe('<img src="{}" height="50/>"'.format(img.images.url))