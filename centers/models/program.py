from django.db import models


class Program(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()

    class Meta:
        app_label = 'centers'
