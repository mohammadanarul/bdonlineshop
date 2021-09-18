from shop.models import Product
from orders.models import OrderItem, Order

def best_sell_product(request):
    order_item = OrderItem.objects.filter(ordered=True)[:2]
    return order_item