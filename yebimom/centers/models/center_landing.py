from django.core.urlresolvers import reverse
from django.db import models
from centers.models.center import Center
from django.db.models.signals import post_save
from django.dispatch import receiver
from centers.utils.center_landing_hashids import get_encoded_center_landing_hashid
from api.tasks.shorten import url_builder, shorten_url

from yebimom.settings import YEBIMOM_URL


class CenterLandingManager(models.Manager):
    pass


class CenterLanding(models.Model):
    objects = CenterLandingManager()

    hash_id = models.CharField(max_length=12, unique=True, blank=True, null=True)
    center = models.ForeignKey(Center)

    title = models.CharField(max_length=200, blank=True, null=True)

    shorten_url = models.CharField(max_length=32, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("landing", kwargs={'slug': self.center.slug, 'hash_id': self.hash_id})

    def get_full_absolute_url(self):
        return YEBIMOM_URL + self.get_absolute_url()


@receiver(post_save, sender=CenterLanding)
def _create_center_landing(sender, instance, created, **kwargs):
    if created:
        instance.hash_id = get_encoded_center_landing_hashid(instance.id)

        instance.save()

        # Create Shorten URL via goo.gl
        full_url = instance.get_full_absolute_url()

        instance_campaign_name = "landing-%s" % (instance.hash_id)
        full_url_with_utm_params = url_builder(
            full_url,
            utm_source="yebimom",
            utm_medium="yebimom",
            utm_campaign=instance_campaign_name)

        result = shorten_url.delay(full_url_with_utm_params)
        instance.shorten_url = result.get()

        instance.save()
