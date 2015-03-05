from django.db import models


class Facility(models.Model):
    name = models.CharField(max_length=40)
    is_available = models.BooleanField(default=False)
    center = models.ForeignKey('Center')

    def __unicode__(self):
        return unicode(self.name)
