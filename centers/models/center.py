from django.db import models

# Model Helper
from django.db.models.signals import post_save

# Util
from centers.utils.center_hashids import get_encoded_center_hashid


class Center(models.Model):
    region = models.ForeignKey("RegionThirdLayer")

    name = models.CharField(max_length=60)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    hash_id = models.CharField(max_length=12, unique=True)

    def __unicode__(self):
        return unicode(self.name)


def update_center_hash_id(sender, instance, created, **kwargs):
    if created:
        # Update hash_id
        instance.hash_id = get_encoded_center_hashid(instance.id)
        instance.save()

post_save.connect(update_center_hash_id, sender=Center)
