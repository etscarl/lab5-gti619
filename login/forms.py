from django import forms
from login.models import *

class LoginForm(forms.Form):
	username = forms.CharField(max_length=16)
	password = forms.CharField(max_length=256, widget=forms.PasswordInput)
	
	def clean(self):
		username = self.cleaned_data['username']
		password = self.cleaned_data['password']
		
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			user = None
			
		if user is not None and user.password == password:
			return self
		
		raise forms.ValidationError(u'Username or Password is incorrect.')
		
class SignUpForm(forms.Form):	
	username = forms.CharField(max_length=16)
	password = forms.CharField(max_length=256, widget=forms.PasswordInput)
	confirmPassword = forms.CharField(max_length=256,widget=forms.PasswordInput,label='Confirm Password')
	role = forms.ChoiceField(choices =[(tag, tag.value) for tag in Roles], label='Role', initial='', widget=forms.Select(), required=True)
	
	def clean_username(self):
		username = self.cleaned_data['username']
		
		if User.objects.filter(username=username).count() == 0:
			return username
		
		raise forms.ValidationError(u'Username "%s" is already in use.' % username)
	
	def clean(self):
		password = self.cleaned_data['password']
		confirmPass = self.cleaned_data['confirmPassword']
		
		if len(password) < 7:
			raise forms.ValidationError(u'Password must be at least 8 characters')
			
		if password != confirmPass:
			raise forms.ValidationError(u'Password and Confirm Password do not match.')
			
		return self