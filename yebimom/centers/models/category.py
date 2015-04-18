from django.db import models
from centers.models.center import Center


class Category(models.Model):
    centers = models.ManyToManyField(Center)

    name = models.CharField(max_length=40, unique=True)
    slug = models.CharField(max_length=20, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return unicode(self.name)
