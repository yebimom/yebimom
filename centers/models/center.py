from django.db import models
from centers.models.program import Program
from centers.models.facility import Facility
from centers.models.policy import Policy


class Center(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=45)
    url = models.URLField()
    program = models.ForeignKey('Program')
    facility = models.ForeignKey('Facility')
    policy = models.ForeignKey('Policy')
