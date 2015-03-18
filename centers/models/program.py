from django.db import models
from centers.models.center import Center


class Program(models.Model):
    center = models.ForeignKey(Center, related_name='program_set')

    name = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return unicode(self.name)
