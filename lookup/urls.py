#This is my views.py file
from django.urls import path
from . import views

urlpatterns = [
    # https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=F3ECAC13-90C4-4ADD-93D3-7284B0A5138A
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
]
