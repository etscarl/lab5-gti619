from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from enum import Enum

class Roles(Enum):	 # A subclass of Enum
	ADMIN = "Administrateur"
	CR = "Clients Résidentiels"
	CA = "Clients D'affaire"

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	email_confirmed = models.BooleanField(default=False)
	role = models.CharField(max_length=5,choices=[(tag,tag.value) for tag in Roles], default=Roles.ADMIN)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
