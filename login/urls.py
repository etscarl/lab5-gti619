from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib import admin

#Create the path for the Login view   
urlpatterns = [
    url('index', views.index, name='index'),
	url('login', views.login, name='login'),
	url('signup', views.signup, name='signup')
]