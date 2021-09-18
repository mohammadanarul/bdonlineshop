from django import template
from shop.models import Product
from orders.models import OrderItem
from datetime import datetime, timedelta
from django.db.models import Sum

# import datetime
register = template.Library()

@register.simple_tag
def best_selling_product(num=20):
    best_sell_item = Product.objects.filter(
        order_item__date_added__lte=datetime.today(),
        order_item__date_added__gt=datetime.today()-timedelta(days=7),
        order_item__ordered=True
        ).annotate(quantity_sum=Sum('order_item__quantity')).order_by('-quantity_sum')[:num]
    return best_sell_item

'''
expiring_soon = Promotion.objects.filter(end_date = datetime.now().date() + timedelta(days=7))
'''