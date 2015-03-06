from django.test import TestCase
from hashids import Hashids
from yebimom.settings.partials.application import HASHIDS_CENTER_SALT

# Util
from centers.utils.center_hashids import get_center_hashids_object
from centers.utils.center_hashids import get_encoded_center_hashid
from centers.utils.center_hashids import get_decoded_center_hashid

# Exceptions
from django.core.exceptions import ObjectDoesNotExist


class CenterHashidsTest(TestCase):

    def setUp(self):
        self.hashids = Hashids(salt=HASHIDS_CENTER_SALT, min_length=5)
        self.instance_id = 123

    def test_center_hashids_object_should_be_returned(self):
        try:
            get_center_hashids_object()
        except ObjectDoesNotExist:
            self.fail("fail to create hashids object")

    def test_encode_center_hashid_should_return_encoded_value(self):
        self.assertEqual(
            get_encoded_center_hashid(self.instance_id),
            self.hashids.encode(self.instance_id)
        )

    def test_decode_center_hashid_should_return_decoded_value(self):
        self.encoded_hashid = self.hashids.encode(self.instance_id)
        self.assertEqual(
            get_decoded_center_hashid(self.encoded_hashid),
            self.hashids.decode(self.encoded_hashid)
        )
