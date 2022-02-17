
from django.http import Http404
from django.shortcuts import render

#used within endpoint class-based view methods:

from .serializers import MusicSerializer 

#parent class for our class-based views. Takes care of method routing
from rest_framework.views import APIView 

#function call that converts our data into a JSON string literal, sends to the client 
from rest_framework.response import Response 

#Status is an enum, a collection of values, that specify status code we would like to send back in the response.
from rest_framework import status
from .models import Music_Catalog
# Create your views here.

class MusicRetrieve(APIView):

    def get(self, request):
        music_catalog = Music_Catalog(music_catalog, many=True)
        serializer = MusicSerializer(music_catalog, many=True)
        return Response(serializer.data)

def post(self, request):
    serializer = MusicSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class MusicDetail(APIView):
#get by id
  def get_music_catalog(self, pk):
    try:
      return Music_Catalog.objects.get(pk=pk)
    except Music_Catalog.DoesNotExist:
      raise Http404

  def get(self, request, pk):
    music_catalog = self.get_music_catalog(pk)
    serializer = MusicSerializer(music_catalog)
    return Response(serializer.data)

 #update
  def put(self,request, pk):
    song = self.get_music_catalog(pk)
    serializer = MusicSerializer(song, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #delete
  def delete(self, request, pk):
    song = self.get_music_catalog(pk)
    song.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)