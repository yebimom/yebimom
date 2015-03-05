from django.db import models


class Program(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    center = models.ForeignKey('Center')

    def __unicode__(self):
        return unicode(self.name)
