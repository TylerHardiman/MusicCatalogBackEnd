

from rest_framework import serializers
from .models import Music_Catalog

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music_Catalog
        fields = ["id", "title", "artist", "album", "genre", "release_date"]