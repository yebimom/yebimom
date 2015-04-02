# encoding: utf-8

from django.db import models
from users.models.user import User
from centers.models.center import Center


class Review(models.Model):
    user = models.ForeignKey(User)
    center = models.ForeignKey(Center)

    def __unicode__(self):
        return u"'%s'에 '%s'님이 남긴 리뷰" % (
            self.center.name,
            self.user.username,
        )

    class Meta:
        unique_together = (('user', 'center'),)
        abstract = True


class VisitReview(Review):
    content = models.TextField()


class ExperienceReview(Review):
    content = models.TextField()
