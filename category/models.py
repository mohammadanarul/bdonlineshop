from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    name = models.CharField(max_length=255, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name
    
    class MPTTMeta:
        order_insertion_by = ['name']
    
    def get_category_absolute_url(self):
        return reverse("category:category_list", kwargs={"slug": self.slug})
    
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
