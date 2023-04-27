from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('meeting_raiting/', MeetingRatingCreateView.as_view(), name='meeting_raiting'),
    path('add_meeting/', MeetingCreateView.as_view(), name='add_meeting'),
    path('meeting/', meeting, name='meeting'),
    path('bars/', BarView.as_view(), name='bars'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile, name='profile'),
    path('place_rating/', PlacesRatingCreateView.as_view(), name="place_rating"),
    path('cafe/', CafeView.as_view(), name='cafe'),
    path('restaurants/', RestaurantView.as_view(), name='restaurants'),
]
