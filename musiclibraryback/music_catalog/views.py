from django.shortcuts import render
from .models import Music_Catalog
from .serializers import MusicSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class MusicRetrieve(APIView):

    def get(self, request):
        music_catalog = Music_Catalog.objects.all()
        serializer = MusicSerializer(music_catalog, many=True)
        return Response(serializer.data)

def post(self, request):
    serializer = MusicSerializer(data=request.request)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)