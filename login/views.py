from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from login.forms import *

# Create your views here.
def index(request):
	return HttpResponse('Index');

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			pass
	else:
		form = LoginForm()	
	return render(request, 'login/login.html', {'form': form})

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			pass
	else:
		form = SignUpForm()	
	return render(request, 'login/signup.html', {'form': form})
	
