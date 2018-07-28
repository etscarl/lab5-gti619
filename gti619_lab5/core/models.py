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
	role = models.CharField(max_length=5,choices=[(tag.value,tag.value) for tag in Roles])

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)		
	instance.profile.save()

class Config(models.Model):
	isPeriodicChange = models.BooleanField(default=False)
	pwdMinLength = models.PositiveIntegerField(default=8)
	pwdMaxLength = models.PositiveIntegerField(blank=True, null=True)
	mustHaveUppercase = models.BooleanField(default=False)
	mustHaveLowercase = models.BooleanField(default=False)
	mustHaveSpecialChar = models.BooleanField(default=False)
	mustHaveNumericChar = models.BooleanField(default=False)
	cannotUsePreviousPWD = models.BooleanField(default=False)
	maxNumberAttemps = models.PositiveIntegerField(default=3)
	delayBetweenAttemps = models.PositiveIntegerField(default=1)
	contactAdminAfterFailure = models.BooleanField(default=False)
