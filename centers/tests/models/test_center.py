# -*- coding: utf-8 -*-

# Model
from centers.models.center import Center

# Test
from centers.tests.models.test_region import RegionAllLayerTest

# Util
from centers.utils.center_hashids import get_encoded_center_hashid
from centers.utils.center_hashids import get_center_hashids_object


class CenterTest(RegionAllLayerTest):

    def setUp(self):
        self.hashids = get_center_hashids_object()
        super(CenterTest, self).setUp()

    def test_encoded_center_hashids_should_have_valid_value(self):
        center = Center.objects.create(
            name="test",
            region_third_layer=self.region_third_layer_0
        )
        updated_center = Center.objects.get(pk=center.pk)
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

    def test_update_center_region_should_change_all_regions(self):
        """
        in current region implementation,
        region_first_layer and region_second_layer value is automatically saved
        depending on region_third_layer value

        region_first_layer and region_second_layer value should automatically update
        when region_third_layer value is updated
        """

        # Create a Center
        # RFL_0 RSL_0 RTL_0
        center = Center.objects.create(
            name="test",
            region_third_layer=self.region_third_layer_0
        )

        # Update a Center
        # RFL_0 RSL_1 RTL_2
        center.region_third_layer = self.region_third_layer_2
        center.save()

        self.assertEqual(
            center.region_second_layer,
            self.region_second_layer_1
        )
