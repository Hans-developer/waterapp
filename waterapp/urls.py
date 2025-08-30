from django.urls import path 
from . import views

urlpatterns = [
    path('', views.clima_view, name='clima_view'),
]