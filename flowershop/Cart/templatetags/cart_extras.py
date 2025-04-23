from django import template

register = template.Library()

@register.filter
def calc_total_price(cart_items):
    return sum(item.quantity * item.product.price for item in cart_items)