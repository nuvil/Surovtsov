from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from catalog.models import *


# Create your views here.
class BarApiView(generics.ListCreateAPIView):
    queryset = Bar.objects.all()
    serializer_class = BarsModelSerializers


class BarsApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bar.objects.all()
    serializer_class = BarsModelSerializers


class RestaurantApiView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantsModelSerializers


class RestaurantsApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantsModelSerializers


class CafApiView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = CafeModelSerializers


class CafeApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = CafeModelSerializers
