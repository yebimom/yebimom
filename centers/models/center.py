from django.db import models

# Model Helper
from django.dispatch import receiver
from django.db.models.signals import post_save

# Util
from centers.utils.center_hashids import get_encoded_center_hashid


class Center(models.Model):
    region = models.ForeignKey("RegionThirdLayer")

    name = models.CharField(max_length=60)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    hash_id = models.CharField(
        "center's_private_unique_id",
        max_length=12,
        unique=True
    )

    def __unicode__(self):
        return unicode(self.name)


@receiver(post_save, sender=Center)
def _update_center_hash_id(sender, instance, created, **kwargs):
    """
    This is sent at the end of a Center's save() method.

    # Features
    - Generate hash_id property, from center's id
    """

    if created:
        instance.hash_id = get_encoded_center_hashid(instance.id)
        instance.save()
