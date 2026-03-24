from django.db import models

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=200)
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.BigIntegerField()
    shop_id = models.ForeignKey(to=Shop, on_delete=models.CASCADE)
    is_sell = models.BooleanField(default=False)
class Date(models.Model):
    date= models.DateField()
    year= models.IntegerField()
    
class Country(models.Model):
    name = models.CharField          

