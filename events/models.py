from django.db import models


class Event(models.Model):
    template_contents = models.TextField(null=True)
    is_in_progress = models.BooleanField(default=True)
