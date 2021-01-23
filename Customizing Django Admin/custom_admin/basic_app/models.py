from django.db import models

# Create your models here.


class Movie(models.Model):

    title = models.CharField(max_length=256)
    length = models.PositiveIntegerField()
    release_year = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Audience(models.Model):

    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    contact = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name +' '+ self.last_name
