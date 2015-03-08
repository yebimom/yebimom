# -*- coding: utf-8 -*-

from django.test import TestCase

# Model
from centers.models.center import Center

# Test
from centers.tests.models.test_region import RegionAllLayerTest

# Util
from centers.utils.center_hashids import get_encoded_center_hashid
from centers.utils.center_hashids import get_center_hashids_object


class CenterTest(RegionAllLayerTest, TestCase):

    def setUp(self):
        self.hashids = get_center_hashids_object()
        super(CenterTest, self).setUp()


    def test_encoded_center_hashids_should_have_valid_value(self):
        center = Center.objects.create(
            name="test",
            region_third_layer=self.region_third_layer_0
        )
        updated_center = Center.objects.get(pk=center.pk)
        print "updated_center:", updated_center, updated_center.hash_id
        self.assertEqual(
            updated_center.hash_id,
            get_encoded_center_hashid(center.id)
        )

    def test_center_should_update_hash_id(self):
        center = Center.objects.create(
            name="test",
            region_third_layer=self.region_third_layer_0
        )
        updated_center = Center.objects.get(pk=center.pk)
        self.assertTrue(
            updated_center.hash_id != ''
        )

    def test_center_should_have_regions_information(self):
        center = Center.objects.create(
            name="test",
            region_third_layer=self.region_third_layer_0
        )

        self.assertEqual(
            center.region_second_layer,
            self.region_second_layer_0
        )

        self.assertEqual(
            center.region_first_layer,
            self.region_first_layer_0
        )
