from django.urls import path, include
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('feedback/', feedback, name='feedback'),
    path('guest/', GuestView.as_view(), name='guest'),
    path('host/', MeetingCreateView.as_view(), name='host'),
    path('institution/', institution, name='institution'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]
