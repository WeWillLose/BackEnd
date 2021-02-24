from django.db import models


def get_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


# Create your models here.

class File(models.Model):
    name = models.CharField(max_length=50, db_index=True, unique=True, null=False)
    file = models.FileField(upload_to=get_path)
