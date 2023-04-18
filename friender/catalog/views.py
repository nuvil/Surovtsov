from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.models import User
from .models import *


# Create your views here.
def home(request):
    # usernames = None
    # usernames = request.user.username
    # print(usernames)
    # user = User.objects.get(username=usernames)
    # print(user.id)
    return render(request, 'home.html')


def feedback(request):
    return render(request, 'feedback.html')


class GuestView(ListView):
    model = Users
    context_object_name = 'users'
    permission_required = 'catalog.view_users'
    template_name = 'guest.html'


# class HostView(ListView):
#     model = Users
#     context_object_name = 'users'
#     permission_required = 'catalog.view_users'
#     template_name = 'host.html'


def institution(request):
    return render(request, 'institution.html')


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
        return redirect('home')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "login.html"

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


# переделать
class MeetingCreateView(CreateView):
    template_name = 'host.html'
    model = Meetings
    fields = ['meeting_name', 'user', 'place']
    success_url = reverse_lazy('home')
