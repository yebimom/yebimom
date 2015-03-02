# -*- coding:utf-8 -*-

# Django Models
from django.db import models
from django.contrib.auth.models import User

# Django Models Helpers
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, primary_key=True)
    nickname = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    is_male = models.BooleanField(default=True)


def create_user_profile(sender, instance, created, **kwargs):
    """
    User객체가 생성되면 User Profile을 생성
    """

    if created:
        # Create UserProfile
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)