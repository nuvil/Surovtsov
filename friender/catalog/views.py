from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from .models import *


# Create your views here.
def home(request):
    return render(request, 'home.html')


def feedback(request):
    return render(request, 'feedback.html')


def guest(request):
    return render(request, 'guest.html')


def host(request):
    return render(request, 'host.html')


def institution(request):
    return render(request, 'institution.html')


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy("login")
