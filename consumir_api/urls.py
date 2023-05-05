from django.urls import path
from . import views

urlpatterns = [
    path('', views.canales, name = 'canales'),
]