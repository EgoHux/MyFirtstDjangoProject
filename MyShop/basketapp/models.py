from django.db import models
from django.conf import settings
from mainapp.models import Product
from django.contrib.auth import get_user_model
# Create your models here.

class BasketManager(models.Manager):
    def sum(self):
        return sum([item.quantity * item.product.price for item in self.all()])

    def quantity(self):
        return sum([item.quantity for item in self.all()])

class Basket(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete= models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    add_time = models.DateTimeField(auto_now_add=True)
    objects = BasketManager()

    def __str__(self):
        return f"{self.product} - {self.quantity}шт"