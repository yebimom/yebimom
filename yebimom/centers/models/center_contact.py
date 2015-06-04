from django.db import models
from centers.models.center import Center
from django.db.models.signals import post_save
from django.dispatch import receiver


class CenterContactManager(models.Manager):
    pass


class CenterContact(models.Model):
    objects = CenterContactManager()

    center = models.ForeignKey(Center)

    def get_managers(self):
        return self.center.managers.all()
    managers = property(get_managers)


@receiver(post_save, sender=CenterContact)
def _create_center_contact(sender, instance, created, **kwargs):
    if created:
        pass
