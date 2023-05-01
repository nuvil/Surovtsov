from rest_framework import serializers
from catalog.models import *


class BarsModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bar
        fields = ['id', 'place_name', 'address', 'place_phone', 'place_site', 'average_paycheck', 'description',
                  'place_photo']


class RestaurantsModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'place_name', 'address', 'place_phone', 'place_site', 'average_paycheck', 'description',
                  'place_photo']

class CafeModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cafe
        fields = ['id', 'place_name', 'address', 'place_phone', 'place_site', 'average_paycheck', 'description',
                  'place_photo']