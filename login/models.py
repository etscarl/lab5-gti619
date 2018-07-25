from django.db import models
from enum import Enum

class Roles(Enum):	 # A subclass of Enum
	ADMIN = "Administrateur"
	CR = "Clients Résidentiels"
	CA = "Clients D'affaire"

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=16)
	password = models.CharField(max_length=256)
	role = models.CharField(max_length=5,choices=[(tag, tag.value) for tag in Roles])
