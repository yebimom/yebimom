from django.db import models
from centers.models.center import Center


class Policy(models.Model):

    class Meta:
        verbose_name_plural = "Policies"

    center = models.ManyToManyField(Center, blank=True)
    name = models.CharField(max_length=40, unique=True)

    def __unicode__(self):
        return unicode(self.name)
