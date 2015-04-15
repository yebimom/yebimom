# -*- coding: utf-8 -*-

from __future__ import absolute_import

# Models
from django.db import models
from django.contrib.auth.models import User

from centers.models import Center
from users.models.favorite import Favorite


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, primary_key=True)
    hash_id = models.CharField("user's hashed id", max_length=16, unique=True)

    nickname = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    is_male = models.BooleanField(default=True)

    favorites = models.ManyToManyField(Center, through=Favorite)

    def __unicode__(self):
        return self.user.username
