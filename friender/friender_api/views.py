from django.shortcuts import render
from rest_framework import generics
from .serializers import PlacesModelSerializers
from catalog.models import *


# Create your views here.
class PlacesApiView(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlacesModelSerializers


class PlaceApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlacesModelSerializers
