from django.db import models

# Create your models here.


class Contents(models.Model):
    name = models.CharField(max_length=20, default='')
    director = models.CharField(max_length=20, default='')
