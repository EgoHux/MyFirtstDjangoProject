from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=140, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=140, blank=True)
    image = models.ImageField(upload_to='product_images')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)


    def __str__(self):
        return self.name