from django.db import models
from centers.models.center import Center


class Facility(models.Model):
    center = models.ForeignKey(Center)

    name = models.CharField(max_length=40)
    is_available = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.name)
