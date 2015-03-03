from django.db import models
from centers.models.center import Center


class Program(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    center = models.ForeignKey(Center)

    class Meta:
        app_label = 'centers'
