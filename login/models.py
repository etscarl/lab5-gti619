from django import forms

# Create your models here.
class LoginInfo(forms.ModelForm):
    nameField = forms.CharField(max_length=16)
    passwordField = forms.CharField(widget=forms.PasswordInput)
