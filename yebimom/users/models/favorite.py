from django.db import models

from django.contrib.auth.models import User
from centers.models import Center


class Favorite(models.Model):
    user = models.ForeignKey(User)
    center = models.ForeignKey(Center)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('user', 'center'),)
