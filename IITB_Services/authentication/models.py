from django.db import models

# Create your models here.
class Gulmohar(models.Model):
    
    item_name=models.CharField(max_length=30)
    availability=models.BooleanField(default=True)
    price=models.IntegerField()




