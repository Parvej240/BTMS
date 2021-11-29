from django.urls import path
from .views import *

urlpatterns = [
    path('doctors/', doctorView.as_view(), name='doctor'),
    path('report/', report, name='report'),
    path('booking/<id>/', BookingFormView.as_view(), name='booking'),

]
