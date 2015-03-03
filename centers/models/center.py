from django.db import models


class Center(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=45)
    url = models.URLField()
