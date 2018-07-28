from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from gti619_lab5.core.models import *

class SignUpForm(UserCreationForm):
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	role = forms.ChoiceField(choices =[(tag, tag.value) for tag in Roles], label='Role', initial='', widget=forms.Select(), required=True)
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2', 'role')
