from django.urls import path
from .views import *

app_name = 'aapp'

urlpatterns = [
    path('', index_view, name='index'),
]