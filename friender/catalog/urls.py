from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile, name='profile'),
    path('meeting/', all_meeting, name='meeting'),
    path('meeting/<int:meeting_id>', meeting_about, name='meeting_about'),
    path('add_meeting/', MeetingCreateView.as_view(), name='add_meeting'),
    path('meeting_raiting/', MeetingRatingCreateView.as_view(), name='meeting_raiting'),
    path('cafe/', CafeView.as_view(), name='cafe'),
    path('restaurants/', RestaurantView.as_view(), name='restaurants'),
    path('bars/', BarView.as_view(), name='bars'),
    path('place_rating/', PlacesRatingCreateView.as_view(), name="place_rating"),
    path('user_rating/', UserRatingCreateView.as_view(), name='user_rating'),
]
