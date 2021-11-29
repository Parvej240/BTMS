from django.urls import path
from .views import *

urlpatterns = [
    path('product/', productview, name='product'),

]
