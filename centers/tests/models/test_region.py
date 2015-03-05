# -*- coding: utf-8 -*-

# Test
from django.test import TestCase

# Models
from centers.models.center import Center
from centers.models.region import RegionFirstLayer
from centers.models.region import RegionSecondLayer
from centers.models.region import RegionThirdLayer


class RegionAllLayerTest(TestCase):
    def setUp(self):
        self.region_first_layer = RegionFirstLayer.objects.create(name="first_layer")
        self.region_second_layer = RegionSecondLayer.objects.create(
            name="second_layer",
            first_layer = self.region_first_layer
        )
        self.region_third_layer = RegionThirdLayer.objects.create(
            name="third_layer",
            second_layer = self.region_second_layer
        )

        for i in range(100):
            Center.objects.create(
                name = "center_%s" % i,
                region = self.region_third_layer
            )


    def test_region_third_layer_should_return_centers_list(self):
        """
        RegionThirdLayer 객체는
        그 지역에 포함되어 있는 모든 산후조리원 리스트를 가져올 수 있어야 한다.
        """

        try:
            self.region_third_layer.centers()
        except:
            self.fail("RegionThirdLayer should have return all centers lists")


    def test_region_third_layer_should_return_centers_list_with_filter(self):
        """
        RegionThirdLayer 객체는
        filter를 통해서 그 지역에 포함되어 있는 산후조리원 중
        검색 조건에 맞는 산후조리원 리스트를 가져올 수 있어야 한다.
        """

        self.assertEqual(
            self.region_third_layer.centers().filter(name="center_0")[0],
            Center.objects.first()
        )

    def test_region_second_layer_should_return_centers_list(self):
        """
        RegionSecondLayer 객체는
        그 지역에 포함되어 있는 모든 산후조리원 리스트를 가져올 수 있어야 한다.
        """

        try:
            self.region_second_layer.centers()
        except:
            self.fail("RegionSecondLayer should have return all centers lists")
