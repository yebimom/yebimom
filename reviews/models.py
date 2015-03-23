from django.db import models
from users.models.user import User
from centers.models.center import Center


class Review(models.Model):

    class Meta:
        unique_together = (('user', 'center'),)

    user = models.ForeignKey(User)
    center = models.ForeignKey(Center)

    content = models.CharField(max_length=255)

    def __unicode__(self):
        return u"%s %s" % (
            self.center.name,
            self.user.username,
        )
