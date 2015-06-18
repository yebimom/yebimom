from django.db import models
from centers.models.center import Center
from centers.models.center_landing import CenterLanding
from django.db.models.signals import post_save
from django.dispatch import receiver


class CenterContactManager(models.Manager):
    pass


class CenterContact(models.Model):
    objects = CenterContactManager()

    center = models.ForeignKey(Center)
    center_landing = models.ForeignKey(CenterLanding)

    name = models.CharField(max_length=16, blank=True, null=True)
    phonenumber = models.CharField(max_length=16, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def get_managers(self):
        return self.center.managers.all()
    managers = property(get_managers)


@receiver(post_save, sender=CenterContact)
def _create_center_contact(sender, instance, created, **kwargs):
    if created:
        # Send SMS to CenterAdmin
        # Send SMS to User
        pass
