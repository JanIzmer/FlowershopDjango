from django.db import models
from django.utils import timezone
from title.models import Product
from Customer.models import Customer

class Order(models.Model):
    customer = models.ForeignKey("Customer.Customer", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    shipping_address = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, default='Pending')
    
    def __str__(self):
        return f"Order {self.id} by {self.customer.user.username}"
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey("title.Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.product_name} in Order {self.order.id}"

# Create your models here.
