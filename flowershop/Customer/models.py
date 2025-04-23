from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(blank=True, max_length=10)
    secondname = models.CharField(blank=True, max_length=10)
    phone = models.CharField(max_length=11)
    email = models.EmailField(blank=True, max_length=20)
    address = models.TextField(blank=True, null=True)
# Create your models here.
