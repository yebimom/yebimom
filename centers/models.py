from django.db import models


class Center(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=45)
    url = models.URLField()


class Program(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()


class Facility(models.Model):
    private_bathroom = models.BooleanField()
    hip_bath = models.BooleanField()
    television = models.BooleanField()
    computer = models.BooleanField()
    freezer = models.BooleanField()


class Policy(models.Model):
    is_delivery_available = models.BooleanField()
    is_husband_visitation_available = models.BooleanField()
    is_parents_visitation_available = models.BooleanField()
