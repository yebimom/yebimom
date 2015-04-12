# encoding: utf-8

from django.db import models
from users.models.user import User
from centers.models.center import Center


class BaseReview(models.Model):
    user = models.ForeignKey(User)
    center = models.ForeignKey(Center)
    content = models.TextField()

    def __unicode__(self):
        return u"%s's review on %s : %s" % (
            self.center.name,
            self.user.username,
            self.content
        )

    class Meta:
        unique_together = (('user', 'center'),)
        abstract = True


class VisitReview(BaseReview):
    pass


class UseReview(BaseReview):
    pass
