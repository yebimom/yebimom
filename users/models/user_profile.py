# -*- coding: utf-8 -*-

# Models
from django.db import models
from django.contrib.auth.models import User

# Models Helper
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, primary_key=True)
    nickname = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    is_male = models.BooleanField(default=True)

    class Meta:
        app_label = 'users'


def create_user_profile(sender, instance, created, **kwargs):
    """
    User 객체가 생성되는 시점에
    post_save Signal을 이용해서 UserProfile 객체를 생성한다
    """

    if created:
        # Create UserProfile
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)
