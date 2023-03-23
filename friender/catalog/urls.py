from django.urls import path, include
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('feedback/', feedback, name='feedback'),
    path('guest/', guest, name='guest'),
    path('host/', host, name='host'),
    path('institution/', institution, name='institution'),
]
