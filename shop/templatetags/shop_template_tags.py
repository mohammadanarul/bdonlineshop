from django import template
from django.db.models import Avg
from shop.models import Product, ReviewRating

register = template.Library()


@register.simple_tag()
def recent_product_tag():
    product = Product.objects.all().order_by('-last_view')[:10]
    return product