from rest_framework import generics, views
from .serializers import *
from catalog.models import *
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response


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
    queryset = Cafe.objects.all()
    serializer_class = CafeModelSerializers


class CafeApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cafe.objects.all()
    serializer_class = CafeModelSerializers


class CafeFileUploadView(views.APIView):
    parser_classes = [FileUploadParser]

    def put(self, request, pk, format=None):
        file_obj = request.data['file']
        obj = Cafe.objects.get(pk=pk)
        obj.photo = file_obj
        obj.save()
        return Response(status=204)
