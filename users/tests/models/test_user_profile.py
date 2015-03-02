from django.test import TestCase


# Django Models
from django.contrib.auth.models import User
from users.models import UserProfile

# Django Exceptions
from django.core.exceptions import ObjectDoesNotExist


class UserProfileTest(TestCase):

    def test_user_profile_should_created_after_user_save(self):
        user = User.objects.create_user(username="test_username")
        try:
            user.userprofile
        except:
            self.fail("User Profile should be created after User save")
