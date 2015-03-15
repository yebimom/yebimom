from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255)
    contents = models.TextField(blank=True, null=True)

    starts_at = models.DateTimeField(blank=True, null=True)
    ends_at = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.title
