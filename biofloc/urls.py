from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage, name='home'),
    path('calculate', Calculate, name='calculate'),
    path('contact', Contact, name='contact'),
    path('report/user', user_report, name='report-user'),
    path('report/download/<id>', report, name='download'),
    path('build/report/download/<id>', builder_download, name='builder_download'),
    path('report/builder/', builder_page, name='builder'),
    path('newsletter', newsletter, name='newsletter'),
    path('start', start_biofloc, name='sb'),
    path('about', about, name='about'),
    path('terms', terms, name='terms'),
    path('policy', policy, name='policy'),
    path('report/all', userreport, name='userreport')
]
