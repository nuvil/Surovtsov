from django import forms
from .models import *


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', ]


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['photo', 'first_name', 'last_name', 'age', 'email', 'address', 'hobbies', 'status']
