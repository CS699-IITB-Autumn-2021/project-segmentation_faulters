from django.db import models
from django.db.models.fields import NullBooleanField

# Create your models here.
class Gulmohar(models.Model):
    
    item_name=models.CharField(max_length=30)
    availability=models.BooleanField(default=True)
    price=models.IntegerField()
    image_src=models.ImageField()




