from django.test import TestCase

from random import random

from hashids import Hashids

from users.utils.user_profile_hashids import get_user_profile_hashids
from users.utils.user_profile_hashids import encode_user_profile_hashids
from users.utils.user_profile_hashids import decode_user_profile_hashids


class HashidsTest(TestCase):
    def setUp(self):
        self.hashids = get_user_profile_hashids()
        self.userprofile_id = int(random() * 1000)

    def test_get_user_profile_hashids_should_return_hashids_object(self):
        self.assertTrue(
            type(self.hashids) is Hashids
        )

    def test_encode_user_profile_hashids_should_return_encoded_value(self):
        self.assertEqual(
            self.hashids.encode(self.userprofile_id),
            encode_user_profile_hashids(self.userprofile_id)
        )

    def test_docode_user_profile_hashids_should_return_decoded_value(self):
        encoded_hashid = self.hashids.encode(self.userprofile_id)
        self.assertEqual(
            self.userprofile_id,
            decode_user_profile_hashids(encoded_hashid),
        )
