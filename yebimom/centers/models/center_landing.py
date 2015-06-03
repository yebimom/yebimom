from django.core.urlresolvers import reverse
from django.db import models
from centers.models.center import Center
from django.db.models.signals import post_save
from django.dispatch import receiver
from centers.utils.center_landing_hashids import get_encoded_center_landing_hashid


class CenterLandingManager(models.Manager):
    pass


class CenterLanding(models.Model):
    objects = CenterLandingManager()

    hash_id = models.CharField(max_length=12, unique=True, blank=True, null=True)
    center = models.ForeignKey(Center)

    def get_absolute_url(self):
        return reverse("landing", kwargs={'slug': self.center.slug, 'hash_id': self.hash_id})


@receiver(post_save, sender=CenterLanding)
def _create_center_landing(sender, instance, created, **kwargs):
    if created:
        instance.hash_id = get_encoded_center_landing_hashid(instance.id)
        instance.save()
