from django.db import models
from centers.models.center import Center


class Program(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    center = models.ForeignKey(Center)

    class Meta:
        app_label = 'centers'
