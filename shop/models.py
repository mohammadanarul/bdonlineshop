from django.db import models
from category.models import Category

class Product(models.Model):
    title               =   models.CharField(max_length=255)
    price               =   models.FloatField(default=1)
    discount_price      =   models.FloatField(default=0)
    category            =   models.ForeignKey(Category, on_delete=models.CASCADE)
    product_details     =   models.TextField()
    image               =   models.ImageField(upload_to='product_images/')
    slug                =   models.SlugField(unique=True, blank=True)
    created_at          =   models.DateTimeField(auto_now_add=True)
    updated_at          =   models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_product_price(self):
        return self.price - self.discount_price

class ProductImages(models.Model):
    product             =   models.ForeignKey(Product, on_delete=models.CASCADE)
    images              =   models.ImageField(upload_to='product_images/')

