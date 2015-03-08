# -*- coding: utf-8 -*-

from django.test import TestCase

# Model
from centers.models.center import Center
from centers.models.region import RegionFirstLayer
from centers.models.region import RegionSecondLayer
from centers.models.region import RegionThirdLayer

# Util
from centers.utils.center_hashids import get_encoded_center_hashid
from centers.utils.center_hashids import get_center_hashids_object


class CenterTest(TestCase):

    def setUp(self):
        """
        각각의 테스트를 수행하기 위해서 초기화 전략은 다음과 같다.

        └── region_first_layer_0 ( RegionFirstLayer )
            └── region_second_layer_0 ( RegionSecondLayer )
                └── region_third_layer_0 ( RegionThirdLayer )
                    └── center_0 ( Center )
                    └── center_1 ( Center )

                └── region_third_layer_1 ( RegionThirdLayer )
                    └── center_2 ( Center )
                    └── center_3 ( Center )

            └── region_second_layer_1 ( RegionSecondLayer )

        └── region_first_layer_1 ( RegionFirstLayer )
        """
        self.hashids = get_center_hashids_object()

        # RegionFirstLayer
        for region_first_layer in range(2):
            RegionFirstLayer.objects.create(
                name="RFL_%s" % region_first_layer
            )

        self.region_first_layer_0 = RegionFirstLayer.objects.first()
        self.region_first_layer_1 = RegionFirstLayer.objects.last()

        # RegionSecondLayer
        for region_second_layer in range(2):
            RegionSecondLayer.objects.create(
                name="RSL_%s" % region_second_layer,
                region_first_layer=self.region_first_layer_0
            )

        self.region_second_layer_0 = RegionSecondLayer.objects.first()
        self.region_second_layer_1 = RegionSecondLayer.objects.last()

        # RegionThirdLayer
        for region_third_layer in range(2):
            RegionThirdLayer.objects.create(
                name="RTL_%s" % region_third_layer,
                region_second_layer=self.region_second_layer_0
            )

        self.region_third_layer_0 = RegionThirdLayer.objects.first()
        self.region_third_layer_1 = RegionThirdLayer.objects.last()

        # Center
        for center in range(2):
            Center.objects.create(
                name="center_%s" % center,
                region_third_layer=self.region_third_layer_0
            )

        for center in range(2, 4):
            Center.objects.create(
                name="center_%s" % center,
                region_third_layer=self.region_third_layer_1
            )

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
