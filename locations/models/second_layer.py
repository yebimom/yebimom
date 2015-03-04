from django.db import models
from locations.models.first_layer import LocationFirstLayer


class LocationSecondLayer(models.Model):
    name = models.CharField(max_length=20)
    first_layer = models.ForeignKey(LocationFirstLayer)

    def __unicode__(self):
        return self.name
