from django.db import models

# Create your models here.
class LoginInfo(models.Model):
    nameField = models.CharField(max_length=16)
    passwordField = models.CharField(max_length=256)

