from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('bars/', BarApiView.as_view(), name="bars_api"),
    re_path('bars/(?P<pk>[\d-]+)', BarsApiView.as_view(), name='bars_api'),
    path('restaurants/', RestaurantApiView.as_view(), name='restaurants_api'),
    re_path('restaurants/(?P<pk>[\d-]+)', RestaurantsApiView.as_view(), name='cafe_api'),
    path('cafe/', CafApiView.as_view(), name='restaurants_api'),
    re_path('cafe/(?P<pk>[\d-]+)', CafeApiView.as_view(), name='cafe_api'),
    re_path('cafe/(?P<pk>[\d-]+)/photo$', CafeFileUploadView.as_view()),
]
