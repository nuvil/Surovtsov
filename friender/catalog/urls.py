from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('feedback/', FeedbackCreateView.as_view(), name='feedback'),
    path('add_meeting/', MeetingCreateView.as_view(), name='add_meeting'),
    path('meeting/', MeetingView.as_view(), name='meeting'),
    path('institution/', institution, name='institution'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]
