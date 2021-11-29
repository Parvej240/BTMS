from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'title', 'details', 'image'
        ]
        widgets = {
            'title': widgets.TextInput(attrs={'placeholder': 'Post Title', 'class': 'form-control mb-4'}),
            'details': widgets.Textarea(attrs={'rows': '3', 'placeholder': 'Post Descriptions', 'class': 'form-control mb-4'}),
        }
