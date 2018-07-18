from django.urls import path
from . import views

#Create the path for the Login view
urlpatterns = [
    path('', views.index, name='index'),
]