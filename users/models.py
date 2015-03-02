# -*- coding:utf-8 -*-

# Django Models
from django.db import models
from django.contrib.auth.models import User

# Django Models Helpers
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, primary_key=True)
