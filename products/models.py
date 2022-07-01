from email.mime import image
from xmlrpc.client import DateTime
from django.db import models

# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.FloatField()
    created_at = models.DateTimeField()
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey('Category',related_name ='m',on_delete=models.CASCADE)



class Category(models.Model):
    name = models.CharField(max_length=100)
