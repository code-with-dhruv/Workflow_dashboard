from django.db import models
from datetime import datetime,date

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=15,null=True)
    email = models.EmailField(auto_now_add=True,null=True)


    date_created=models.DateTimeField()

    def __str__(self):
        return self.name
class Tags(models.Model):
    name=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    CATEGORY=(
        ('')
     )
    name=models.CharField(max_length=50,null=True)
    price=models.FloatField()
    category=models.CharField(max_length=50,null=True,choices=CATEGORY)
    description=models.CharField(max_length=200, null=True,blank=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    tags=models.ManyToManyField(Tags)
class Order(models.Model):
    STATUS =(
        ('pending','pending')
        ('Out for Delivery','Out for Delivery')
        ('Delivered', 'Delivered'),
    )
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)
    