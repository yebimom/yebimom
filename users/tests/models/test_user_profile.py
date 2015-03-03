from django.test import TestCase


# Models
from django.contrib.auth.models import User
from users.models import UserProfile

# Utils
from users.utils.user_profile_hashids import encode_user_profile_hashids

# Exceptions
from django.core.exceptions import ObjectDoesNotExist


class UserProfileTest(TestCase):

    def test_user_profile_should_created_after_user_save(self):
        user = User.objects.create_user(username="test_username")
        try:
            user.userprofile
        except:
            self.fail("User Profile should be created after User save")

    def test_user_profile_should_have_valid_hash_id(self):
        user = User.objects.create_user(username="test_username")
        self.assertEqual(
            user.userprofile.hash_id,
            encode_user_profile_hashids(user.id)
        )
