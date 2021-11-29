from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, User
from django.forms import fields, widgets


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'user_type', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class UpdateUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        widgets = {
            'first_name': widgets.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}),
        }


class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'about', ]
        widgets = {

            'about': widgets.Textarea(attrs={'cols': '35', 'rows': '5', 'placeholder': 'About Me', 'class': 'bg-gray-100 bg-opacity-50 rounded focus:ring-2 mt-2 focus:ring-indigo-200 focus:bg-transparent border border-gray-300 focus:border-indigo-500 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}),
        }
