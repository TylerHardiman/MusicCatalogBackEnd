from pyexpat import _Model
from django.db import models

# Create your models here.
class Music_Catalog(models, _Model):
  title = models.CharField(max_length=50)
  artist = models.CharField(max_length=50)
  album = models.CharField(max_length=50)
  genre = models.CharField(max_length=50)
  release_date = models.DateField()
