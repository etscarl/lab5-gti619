from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib import admin

#Create the path for the Login view   
urlpatterns = [
    url('index', views.index, name='index'),
	url('signup', views.signup, name='signup'),
	url('logout', views.logout, name = 'logout'),
	url('', views.login, name='login')
]