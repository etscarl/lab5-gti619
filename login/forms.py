from django import forms
from django.forms import ModelForm
from login.models import *

class LoginForm(ModelForm):
	confirmPassword = models.CharField(max_length=256)
	class Meta:
		model = LoginInfo
		fields = ['nameField', 'passwordField']
		labels = {
            'nameField': 'Username',
			'passwordField': 'Password'
        }
		
		widgets = {
			'passwordField': forms.PasswordInput(),
		}

class SignUpForm(ModelForm):
	class Meta:
		model = SignUpInfo
		fields = ['nameField', 'passwordField', 'confirmPassword']
		labels = {
			'nameField': 'Username',
			'passwordField': 'Password',
			'confirmPassword': 'Confirm password'
		}