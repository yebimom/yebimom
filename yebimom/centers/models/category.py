from django.db import models
from centers.models.center import Center


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    slag = models.CharField(max_length=20, unique=True, blank=True)
    center = models.ManyToManyField(Center, blank=True)
    name = models.CharField(max_length=40, unique=True)

    def __unicode__(self):
        return unicode(self.name)