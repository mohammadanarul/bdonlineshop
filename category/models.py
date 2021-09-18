from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext_lazy as _

class Category(MPTTModel):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(_("image"), upload_to='category/')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(unique=True, blank=True)
    
    class MPTTMeta:
        order_insertion_by = ['name']
    
    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k= k.parent
        return '/'.join(full_path[::-1])
    
    def get_category_absolute_url(self):
        return reverse("category:category_list", kwargs={"slug": self.slug})
    
    def get_total_product(self):
        return self.products.all().count()
    
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
