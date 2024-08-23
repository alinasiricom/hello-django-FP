from django.urls import path
from .views import *

app_name = 'aapp'

urlpatterns = [
    path('', index_view, name='index'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
]