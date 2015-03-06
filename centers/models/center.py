from django.db import models
from hashids import Hashids
from yebimom.settings.partials.application import HASHIDS_CENTER_SALT

# Model Helper
from django.db.models.signals import post_save


class Center(models.Model):
    region = models.ForeignKey("RegionThirdLayer")

    name = models.CharField(max_length=60)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    hash_id = models.CharField(
        max_length=12, unique=True, default="default")

    def __unicode__(self):
        return unicode(self.name)


def update_center_hash_id(sender, instance, created, **kwargs):
    if created:
        # Update hash_id
        Center.objects.filter(pk=instance.pk).update(
            hash_id=encode_center_hashids(instance.id))

post_save.connect(update_center_hash_id, sender=Center)


# hashids methods
def get_center_hashids():
    return Hashids(salt=HASHIDS_CENTER_SALT, min_length=12)


def encode_center_hashids(center_id):
    hashids = get_center_hashids()
    return hashids.encode(center_id)


def decode_center_hashids(center_hash_id):
    hashids = get_center_hashids()
    return hashids.decode(center_hash_id)
