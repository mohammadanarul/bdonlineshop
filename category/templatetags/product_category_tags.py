from django import template
from category.models import Category

register = template.Library()


@register.simple_tag()
def category_tags():
    category = Category.objects.all()
    return category