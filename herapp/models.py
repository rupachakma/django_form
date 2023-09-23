from django.db import models

# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    department = models.CharField(max_length=20)

    