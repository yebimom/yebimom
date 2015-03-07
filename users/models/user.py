# -*- coding: utf-8 -*-

# Models
from django.contrib.auth.models import User
from users.models.user_profile import UserProfile

# Models Helper
from django.dispatch import receiver
from django.db.models.signals import post_save

# Utils
from users.utils.user_profile_hashids import encode_user_profile_hashids


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    This is sent at the beginning of a User’s save() method.

    # Features
    - Create User Profile object,
      connected with User object via One-to-One field
    """

    if created:
        UserProfile.objects.create(
            user=instance,
            hash_id=encode_user_profile_hashids(instance.id)
        )
