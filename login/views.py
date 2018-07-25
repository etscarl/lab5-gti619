from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from login.forms import *
from login.models import *

# Create your views here.
def index(request):
	if request.session.has_key('username'):
		return HttpResponse('Index');
	else:
		return redirect('/login', {'form': LoginForm()})

def login(request):
	if request.session.has_key('username'):
	  return redirect('/login/index.html')
	else:
		if request.method == 'POST':
			form = LoginForm(request.POST)
			if form.is_valid():
				request.session['username'] = form.data['username']
				return redirect('/login/index.html')
		else:
			form = LoginForm()	
		return render(request, 'login/login.html', {'form': form})

def signup(request):
	if request.session.has_key('username'):
		return redirect('/login/logout/')
	else:
		if request.method == 'POST':
			form = SignUpForm(request.POST)
			if form.is_valid():
				user = User(username=form.data['username'], password=form.data['password'], role=form.data['role'])		
				user.save()
				return render(request, 'login/login.html', {'form': LoginForm()})
		else:
			form = SignUpForm()	
		
		return render(request, 'login/signup.html', {'form': form})

def logout(request):
	try:
		del request.session['username']
		request.session.modified = True
	except:
		pass
	return redirect('/login', {'form': LoginForm()})