from django.db import models
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json
# Create your models here.

class Test(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    code=models.CharField(max_length=10,blank=True,null=True)
    def __str__(self):
        return self.name
    
class Position(models.Model):
    name=models.CharField(max_length=200)
    image=models.URLField()
    price=models.CharField(max_length=200,null=True)
    market_cap=models.CharField(max_length=200,null=True)
    rank=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name