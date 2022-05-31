from pyexpat import model
from django.db import models

# Create your models here.
class TaskTable(models.Model):
    TaskTitle=models.CharField(max_length=50)
    TaskDescriptions=models.CharField(max_length=500)