from django.test import TestCase

from hashids import Hashids

from users.utils import get_user_profile_hashids
from users.utils import encode_user_profile_hashids
from users.utils import decode_user_profile_hashids


class HashidsTest(TestCase):
    def setUp(self):
        self.hashids = get_user_profile_hashids()

    def test_get_user_profile_hashids_should_return_hashids_object(self):
        self.assertTrue(
            type(self.hashids) is Hashids
        )

    def test_encode_user_profile_hashids_should_return_encoded_value(self):
        self.assertEqual(
            self.hashids.encode(1),
            encode_user_profile_hashids(1)
        )

    def test_docode_user_profile_hashids_should_return_decoded_value(self):
        encoded_hashid = self.hashids.encode(1)
        self.assertEqual(
            1,
            decode_user_profile_hashids(encoded_hashid),
        )
