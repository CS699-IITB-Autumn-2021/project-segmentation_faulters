from django.db import models
from django.db.models.fields import CharField, NullBooleanField

# Create your models here.
class Gulmohar(models.Model):
    
    item_name=models.CharField(max_length=30)
    availability=models.BooleanField(default=True)
    price=models.IntegerField()
    image_src=models.ImageField()



class Orders(models.Model):

    order_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, default="hello")
    order_details=models.CharField(max_length=500)
    order_time= models.DateTimeField(auto_now_add=True)
    Vendor = models.CharField(max_length=50)
    Price = models.IntegerField()
    Order_completed = models.BooleanField(default= False)
