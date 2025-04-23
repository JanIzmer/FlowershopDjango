from django.db import models
from Customer.models import Customer
from Order.models import Order, OrderProduct
from django.utils import timezone
from title.models import Product

class Cart(models.Model):
    customer = models.ForeignKey("Customer.Customer", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Cart of {self.customer.user.username}"
    
    def add_to_order(self):
        order = Order.objects.create(
            customer=self.customer,
            shipping_address=self.customer.adres,
            status="Pending"
        )
        for cart_item in self.items.all():
            OrderProduct.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity
            )
        self.items.all().delete()
        return order
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey("title.Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.product_name}"
