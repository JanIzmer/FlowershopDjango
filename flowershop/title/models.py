from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.product_name
    
