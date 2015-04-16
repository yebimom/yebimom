from __future__ import absolute_import

from django.db import models

from centers.models import Center


class Favorite(models.Model):
    user_profile = models.ForeignKey('UserProfile')
    center = models.ForeignKey(Center)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s -> %s" % (
            self.user_profile.user.username,
            self.center.name,
        )

    class Meta:
        unique_together = (('user_profile', 'center'),)
        auto_created = True
