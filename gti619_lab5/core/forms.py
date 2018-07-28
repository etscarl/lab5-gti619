from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from gti619_lab5.core.models import *

class SignUpForm(UserCreationForm):
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	role = forms.ChoiceField(choices =[(tag.value, tag.value) for tag in Roles], label='Role', initial=Roles.ADMIN, widget=forms.Select(), required=True)
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2', 'role')

class ConfigForm(ModelForm):
	class Meta:
		model = Config
		labels = {'isPeriodicChange': 'Password must be changed periodically',
				'pwdMinLength': 'Minimum length for password', 
				'pwdMaxLength': 'Maximum length for password', 
				'mustHaveUppercase': 'Must have at least one uppercase', 
				'mustHaveLowercase': 'Must have at least one lowercase', 
				'mustHaveSpecialChar': 'Must have at least one special character', 
				'mustHaveNumericChar': 'Must have at least one numeric character',
				'cannotUsePreviousPWD': 'User cannot re-use recent previous passwords',
				'maxNumberAttemps': 'Max number of attemps',
				'delayBetweenAttemps': 'Delay between attemps (in minutes)',
				'contactAdminAfterFailure': 'User must contact admin on failure'}

		fields = ['isPeriodicChange', 'pwdMinLength', 'pwdMaxLength', 'mustHaveUppercase', 'mustHaveLowercase', 
		'mustHaveSpecialChar', 'mustHaveNumericChar', 'cannotUsePreviousPWD', 'maxNumberAttemps', 'delayBetweenAttemps', 'contactAdminAfterFailure']