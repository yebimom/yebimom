from django.db import models


class Center(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=45)
    url = models.URLField()
    program = models.ForeignObject('Program')
    facility = models.ForeignKey('Facility')
    policy = models.ForeignKey('Policy')


class Program(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()


class Facility(models.Model):
    name = models.CharField()
    is_available = models.BooleanField()


class Policy(models.Model):
    name = models.CharField()
    is_available = models.BooleanField()
