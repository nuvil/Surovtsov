from rest_framework import serializers
from catalog.models import *


class PlacesModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'place_name', 'address', 'place_phone']
