from django.db import models


# Create your models here.

class ToDo(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
