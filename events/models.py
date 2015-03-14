from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=128)
    template_contents = models.TextField(null=True)
    is_in_progress = models.BooleanField(default=True)
