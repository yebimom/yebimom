from django.db import models
from django.utils import timezone

from django.core.urlresolvers import reverse

from yebimom.models import MetaMixin


def _get_thumbnail_path(self, file_name):
    return "events/%s/%s" % (self.id, file_name)


class Event(MetaMixin):
    title = models.CharField(max_length=255)
    contents = models.TextField(blank=True, null=True)

    starts_at = models.DateTimeField(blank=True, null=True)
    ends_at = models.DateTimeField(blank=True, null=True)

    thumbnail = models.ImageField(
        upload_to=_get_thumbnail_path
    )

    def _is_in_progress(self):
        return self.ends_at > timezone.now()
    is_in_progress = property(_is_in_progress)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('events:detail', args=[str(self.id)])
