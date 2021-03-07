
from django.urls import path, include
from . import views
from django.views import View
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('about/', About.as_view(), name='About'),
    path('contact/', Contact.as_view(), name='Contact'),
    path('team/', Team.as_view(), name='Team'),
    path('projects/', Projects.as_view(), name='Projects'),
    path('service/', Service.as_view(), name='Service'),
]
