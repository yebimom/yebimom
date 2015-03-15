from django.db import models
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=255)
    contents = models.TextField(blank=True, null=True)

    starts_at = models.DateTimeField(blank=True, null=True)
    ends_at = models.DateTimeField(blank=True, null=True)

    thumbnail = models.ImageField(
        upload_to='events'
    )

    def _is_in_progress(self):
        return self.ends_at > timezone.now()
    is_in_progress = property(_is_in_progress)

    def __unicode__(self):
        return self.title
