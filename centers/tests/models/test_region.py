# -*- coding: utf-8 -*-

# Test
from django.test import TestCase

# Models
from centers.models.region import RegionThirdLayer


class RegionAllLayerTest(TestCase):
    def test_region_third_layer_should_return_centers_list(self):
        """
        RegionThirdLayer 객체는
        그 지역에 포함되어 있는 모든 산후조리원 리스트를 가져올 수 있어야 한다.
        """

        # region_third_layer = RegionThirdLayer()
        # try:
        #     region_third_layer.center_set.all()
        # except:
        #     self.fail("RegionThirdLayer should have return all centers lists")

        region_third_layer = RegionThirdLayer()
        try:
            region_third_layer.centers.all()
        except:
            self.fail("RegionThirdLayer should have return all centers lists")
