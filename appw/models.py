from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    contact = models.CharField(default="", max_length=12)
