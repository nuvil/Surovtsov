from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('places/', PlacesApiView.as_view(), name="places_api"),
    re_path('places/(?P<pk>[\d-]+)', PlaceApiView.as_view(), name='places_api'),
]
