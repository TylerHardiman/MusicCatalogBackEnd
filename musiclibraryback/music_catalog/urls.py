from django.urls import path
from serializers import MusicSerializer
urlpatterns = [
    path("musiclibraryback/", MusicSerializer()), #Possible Syntax issue
]