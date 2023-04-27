from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import Group
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.models import User
from .models import *
from .forms import *


# Create your views here.
def home(request):
    return render(request, 'home.html')


class BarView(ListView):
    model = Bar
    paginate_by = 1
    template_name = 'bars.html'
    context_object_name = 'bars'


class CafeView(ListView):
    model = Cafe
    paginate_by = 1
    template_name = 'cafe.html'
    context_object_name = 'cafe'


class RestaurantView(ListView):
    model = Restaurant
    paginate_by = 1
    template_name = 'restaurants.html'
    context_object_name = 'restaurants'


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        user.is_staff = True
        group_reg = Group.objects.get(name='register_users')
        user.groups.add(group_reg)
        user.save()
        login(self.request, user)
        new_user = Users(id_user=user, )
        new_user.save()
        return redirect('login')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "login.html"

    def get_success_url(self):
        return reverse_lazy('meeting')


def logout_user(request):
    logout(request)
    return redirect('login')


# cделать создателя встречи с статусом host
class MeetingCreateView(CreateView):
    template_name = 'add_meeting.html'
    model = Meetings
    fields = ['meeting_name', 'date_meeting', 'time_meeting', 'user', 'place', 'meeting_description']
    success_url = reverse_lazy('meeting')


# class MeetingView(ListView):
#     template_name = 'all_meeting.html'
#     model = Meetings
#     paginate_by = 2
#     # context_object_name = 'meetings'
#     permission_required = 'catalog.view_meeting'


def meeting(request):
    url = reverse(home)
    meetings = Meetings.objects.all()
    paginator = Paginator(meetings, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'all_meeting.html', {"meetings": meetings, 'url': url, 'page_obj': page_obj})


# Рейтинг встречи
class MeetingRatingCreateView(CreateView):
    template_name = 'meeting_rating.html'
    model = Rating
    fields = ['user', 'meetings', 'meetings_rating', 'comment']
    success_url = reverse_lazy('meeting')


class PlacesRatingCreateView(CreateView):
    template_name = 'place_rating.html'
    model = Rating
    fields = ['user', 'place', 'place_rating', 'comment']
    success_url = reverse_lazy('bars')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.users, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.users)
        return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form})
