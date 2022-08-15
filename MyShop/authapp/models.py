from django.db import models
from django.contrib.auth.models import AbstractUser

class ShopUser(AbstractUser):
    avatar = models.ImageField(blank=True, upload_to='user_images')
    age = models.PositiveIntegerField(blank=True, default=0)
    

# Create your models here.
