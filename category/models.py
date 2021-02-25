from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from django.template.defaultfilters import slugify

class Category(MPTTModel):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
    
    def get_category_absolute_url(self):
        return reverse("category:category_list", kwargs={"slug": self.slug})
    
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
