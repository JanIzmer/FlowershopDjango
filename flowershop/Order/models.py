from django.db import models
from django.utils import timezone
from title.models import Product
from Customer.models import Customer

class Order(models.Model):
    DELIVERY_CHOICES = [
    ('courier', 'Kurier'),
    ('pickup', 'Odbiór osobisty'),
]
    STATUS = [
        ('Pending', 'W oczekiwaniu'),
        ('in_delivery', 'W dostawie'),
        ('completed', 'Dostarczone'),
        ('cancelled', 'Anulowane')
    ]
    customer = models.ForeignKey("Customer.Customer", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    shipping_address = models.TextField(blank=True, null=True)
    street = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=50, choices=STATUS, default=STATUS[1])
    delivery_method = models.CharField(max_length=20, choices=DELIVERY_CHOICES, default=DELIVERY_CHOICES[1])

    def get_order_products(self):
        return self.orderproduct_set.all()
    
    def __str__(self):
        return f"Order {self.id} by {self.customer.user.username}"
    
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey("title.Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.product_name} in Order {self.order.id}"

# Create your models here.
