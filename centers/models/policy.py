from django.db import models
from centers.models.center import Center


class Policy(models.Model):
    name = models.CharField(max_length=40)
    is_available = models.BooleanField(default=False)
    center = models.ForeignKey(Center)

    def __unicode__(self):
        return self.name
