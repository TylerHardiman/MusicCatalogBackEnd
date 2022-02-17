from django.db import models
from rest_framework.fields import IntegerField

class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    release_date = models.DateField()
    num_of_likes = IntegerField()
