from django.db import models


class Program(models.Model):
    center = models.ForeignKey('Center')

    name = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return unicode(self.name)
