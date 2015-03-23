from django.db import models
from users.models.user import User
from centers.models.center import Center


class Review(models.Model):

    class Meta:
        unique_together = (('user_id', 'center_id'),)

    user = models.ForeignKey(User)
    center = models.ForeignKey(Center)
