from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'home.html')


class PlaceView(ListView):
    model = Place
    template_name = 'place.html'
    context_object_name = 'places'


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
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


# cделать создателя встречи с статусом host
class MeetingCreateView(CreateView):
    template_name = 'add_meeting.html'
    model = Meetings
    fields = ['meeting_name', 'date_meeting', 'time_meeting', 'user', 'place', 'meeting_description']
    success_url = reverse_lazy('meeting')


# cделать вьюшки встречь
class MeetingView(ListView):
    template_name = 'all_meeting.html'
    model = Meetings
    context_object_name = 'meetings'
    permission_required = 'catalog.view_meeting'


# Рейтинг встречи
class FeedbackCreateView(CreateView):
    template_name = 'feedback.html'
    model = Rating
    fields = ['user', 'meetings', 'meetings_rating', 'comment']
    success_url = reverse_lazy('feedback')


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
