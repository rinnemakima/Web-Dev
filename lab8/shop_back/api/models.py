from django.db import models

# Create your models here.
class Product(models.Model):
  name = models.CharField
  price = models.FloatField
  description = models.TextField
  count = models.IntegerField
  is_active = models.BooleanField(default=True)
  
class Category(models.Model):
  name = models.CharField