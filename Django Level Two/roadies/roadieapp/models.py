from django.db import models

# Create your models here.


class Roadies(models.Model):
    first_name = models.CharField(max_length=364)
    last_name = models.CharField(max_length=364)
