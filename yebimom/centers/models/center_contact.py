from django.db import models
from centers.models.center import Center


class CenterContactManager(models.Manager):
    pass


class CenterContact(models.Model):
    objects = CenterContactManager()

    center = models.ForeignKey(Center)
