from django import forms
from .models import Booking
from django.forms import fields, widgets


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'number', 'problem', 'date']
        widgets = {
            'name': widgets.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}),
            'number': widgets.NumberInput(attrs={'placeholder': 'Number', 'class': 'form-control'}),
            'problem': widgets.TextInput(attrs={'placeholder': 'You Problem in One line', 'class': 'form-control'}),
            'date': widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}),

        }
