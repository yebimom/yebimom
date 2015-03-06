from django.test import TestCase

# Model
from centers.models.center import Center
from centers.models.center import get_center_hashids

# Test
from centers.tests.models.test_region import RegionAllLayerTest


class CenterTest(RegionAllLayerTest, TestCase):

    def setUp(self):
        self.hashids = get_center_hashids()
        super(CenterTest, self).setUp()

    def test_encoded_center_hashids_should_have_valid_value(self):
        center = Center.objects.create(
            name="test",
            region=self.region_third_layer_0
        )
        updated_center = Center.objects.get(pk=center.pk)
        print "updated_center:", updated_center, updated_center.hash_id
        self.assertEqual(
            updated_center.hash_id,
            self.hashids.encode(center.id)
        )

    def test_center_should_update_hash_id(self):
        center = Center.objects.create(
            name="test",
            region=self.region_third_layer_0
        )
        updated_center = Center.objects.get(pk=center.pk)
        self.assertTrue(
            updated_center.hash_id != ''
        )
