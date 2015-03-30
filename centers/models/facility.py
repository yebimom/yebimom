from django.db import models
from centers.models.center import Center


class Facility(models.Model):

    class Meta:
        verbose_name_plural = "Facilities"

    center = models.ManyToManyField(Center, blank=True)
    name = models.CharField(max_length=40, unique=True)

    def __unicode__(self):
        return unicode(self.name)
