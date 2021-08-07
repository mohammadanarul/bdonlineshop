from django.db import models
from django.utils.translation import ugettext_lazy as _
from category.models import Category
from brands.models import Brand
from django.urls import reverse

class Product(models.Model):

    VARIANTS = (
            ('None', 'None'),
            ('Size', 'Size'),
            ('Color', 'Color'),
            ('Size-Color', 'Size-Color'),
    )

    title               =   models.CharField(max_length=255, verbose_name=_("title"))
    price               =   models.FloatField(default=1, verbose_name=_("price"))
    discount_price      =   models.FloatField(default=0, verbose_name=_("discount price"))
    category            =   models.ForeignKey(Category, verbose_name=_('category'), on_delete=models.CASCADE)
    brand               =   models.ForeignKey(Brand, verbose_name=_("brand"), on_delete=models.CASCADE)
    product_details     =   models.TextField(verbose_name=_('priduct details'))
    image               =   models.ImageField(verbose_name=_('image'), upload_to='product_images/')
    variant             =   models.CharField(_("variant"), max_length=15, choices=VARIANTS, default='None')
    slug                =   models.SlugField(verbose_name=_('slug'), unique=True, blank=True)
    created_at          =   models.DateTimeField(verbose_name=_('created at'), auto_now_add=True)
    updated_at          =   models.DateTimeField(verbose_name=_('updated at'), auto_now=True)

    def __str__(self):
        return self.title
    
    def get_product_price(self):
        return self.price - self.discount_price
    
    def get_absolute_url(self):
        return reverse("shop:single_shop_view", kwargs={"slug": self.slug})
    

class ProductImages(models.Model):
    product             =   models.ForeignKey(Product, on_delete=models.CASCADE)
    images              =   models.ImageField(upload_to='product_images/')

