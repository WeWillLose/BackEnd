from django.db import models


# Create your models here.

class Docx(models.Model):
    file = models.BinaryField()
