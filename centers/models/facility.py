from django.db import models


class Facility(models.Model):
    name = models.CharField(max_length=40)
    is_available = models.BooleanField(default=False)

    class Meta:
        app_label = 'centers'
