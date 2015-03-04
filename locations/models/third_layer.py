from django.db import models
from locations.models.second_layer import LocationSecondLayer


class LocationThirdLayer(models.Model):
    name = models.CharField(max_length=20)
    third_layer = models.ForeignKey(LocationSecondLayer)

    def __unicode__(self):
        return self.name
