from django.db.models import Avg, Count
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from category.models import Category
from brands.models import Brand
from django.urls import reverse
from cloudinary.models import CloudinaryField
User = settings.AUTH_USER_MODEL

# class MyCloudinaryField(CloudinaryField):
#     def upload_options(self, model_instance):
#         profile_avatar_name = {'public_id': model_instance.user.id + "-" + model_instance.pk}
#         return profile_avatar_name

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
    category            =   models.ForeignKey(Category, verbose_name=_('category'), related_name='products', on_delete=models.CASCADE)
    brand               =   models.ForeignKey(Brand, verbose_name=_("brand"), on_delete=models.CASCADE)
    product_details     =   models.TextField(verbose_name=_('priduct details'))
    image               =   CloudinaryField(transformation=[{"quality":"auto:best",},{'height': 250, 'width': 250}])
    variant             =   models.CharField(_("variant"), max_length=15, choices=VARIANTS, default='None')
    slug                =   models.SlugField(verbose_name=_('slug'), unique=True, blank=True)
    is_featured         =   models.BooleanField(_("featured"), default=False)
    on_sale             =   models.BooleanField(_("on sale"), default=False)
    created_at          =   models.DateTimeField(verbose_name=_('created at'), auto_now_add=True)
    updated_at          =   models.DateTimeField(verbose_name=_('updated at'), auto_now=True)
    last_view           =   models.DateTimeField(_("last view"), blank=True, null=True)

    def __str__(self):
        return f'{self.pk} of {self.title}'
    
    class Meta:
        ordering = ('-created_at',)
        
    def get_product_price(self):
        return self.price - self.discount_price
    
    def get_absolute_url(self):
        return reverse("shop:single_shop_view", kwargs={"slug": self.slug})
    
    def average_rating(self):
        avg = 0
        reviews = ReviewRating.objects.filter(product=self).aggregate(average=Avg('rating'))
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg
    
    def average_review(self):
        count = 0
        reviews = ReviewRating.objects.filter(product=self).aggregate(count=Count('id'))
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count

    @property
    def best_sell_product(self):
        return self.order_item.filter(ordered=True).count()
    

class ProductImages(models.Model):
    product             =   models.ForeignKey(Product, on_delete=models.CASCADE)
    images              =   CloudinaryField(transformation=[{"quality":"auto:best",},{'height': 250, 'width': 250}])


class ReviewRating(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("item"), related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
    rating = models.FloatField(_("rating"))
    subject = models.CharField(_("subject"), max_length=100)
    review  = models.TextField(_("review"))
    ip = models.CharField(_("ip"), max_length=30)
    status = models.BooleanField(_("status"), default=True)
    last_review = models.DateTimeField(_("last review"), blank=True, null=True)

    def __str__(self):
        return f"{self.subject} - {self.user}"
    
