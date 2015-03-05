# -*- coding: utf-8 -*-

# Models
from django.contrib.auth.models import User
from users.models.user_profile import UserProfile

# Models Helper
from django.db.models.signals import post_save

# Utils
from users.utils.user_profile_hashids import encode_user_profile_hashids


def create_user_profile(sender, instance, created, **kwargs):
    """
    User 객체가 생성되는 시점에
    post_save Signal을 이용해서 UserProfile 객체를 생성하고 초기화한다
    """

    if created:
        # Create UserProfile
        userprofile = UserProfile.objects.create(
            user=instance,
            hash_id=encode_user_profile_hashids(instance.id)
        )

post_save.connect(create_user_profile, sender=User)
