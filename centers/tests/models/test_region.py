# -*- coding: utf-8 -*-

# Test
from django.test import TestCase

# Models
from centers.models.center import Center
from centers.models.region import RegionFirstLayer
from centers.models.region import RegionSecondLayer
from centers.models.region import RegionThirdLayer

# Type
from django.db.models.query import QuerySet


class RegionAllLayerTest(TestCase):
    """
    RegionAllLayer 모델에 대해서 다음의 세 가지 항목을 테스트한다.

    1.
    RegionLayer 모델이 centers() 라는 함수를 통해서
    산후조리원 리스트를 가져올 수 있다

    2.
    RegionLayer 모델이 centers() 라는 함수를 통해서 받는 결과값은
    <class 'django.db.models.query.QuerySet'> 이다.

    이러한 결과값을 리턴할 때만, filter()를 이용하여 조건부 검색이 가능하다.

    3.
    RegionLayer 모델은 실제로 그 지역에 포함되어 있는
    산후조리원 리스트를 가져올 수 있다.
    """

    def setUp(self):
        """
        각각의 테스트를 수행하기 위해서 초기화 전략은 다음과 같다.

        └── region_first_layer_0 ( RegionFirstLayer )
            └── region_second_layer_0 ( RegionSecondLayer )
                └── region_third_layer_0 ( RegionThirdLayer )
                    └── center_0 ( Center )
                    └── center_1 ( Center )

                └── region_third_layer_1 ( RegionThirdLayer )

            └── region_second_layer_1 ( RegionSecondLayer )

        └── region_first_layer_1 ( RegionFirstLayer )
        """

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
                first_layer = self.region_first_layer_0
            )

        self.region_second_layer_0 = RegionSecondLayer.objects.first()
        self.region_second_layer_1 = RegionSecondLayer.objects.last()

        # RegionThirdLayer
        for region_third_layer in range(2):
            RegionThirdLayer.objects.create(
                name="RTL_%s" % region_third_layer,
                second_layer = self.region_second_layer_0
            )

        self.region_third_layer_0 = RegionThirdLayer.objects.first()
        self.region_third_layer_1 = RegionThirdLayer.objects.last()

        # Center
        for center in range(2):
            Center.objects.create(
                name="center_%s" % center,
                region=self.region_third_layer_0
            )

        self.center_0 = Center.objects.first()
        self.center_1 = Center.objects.last()

    def test_region_first_layer_centers_should_return_centers_queryset(self):
        """
        RegionFirstLayer 객체가 centers() 함수를 호출한 결과의 type은
        <class 'django.db.models.query.QuerySet'> 이다.
        """
        self.assertEqual(
            type(self.region_first_layer_0.centers()),
            QuerySet
        )

    def test_region_second_layer_centers_should_return_centers_queryset(self):
        """
        RegionSecondLayer 객체가 centers() 함수를 호출한 결과의 type은
        <class 'django.db.models.query.QuerySet'> 이다.
        """
        self.assertEqual(
            type(self.region_second_layer_0.centers()),
            QuerySet
        )

    def test_region_third_layer_centers_should_return_centers_queryset(self):
        """
        RegionThirdLayer 객체가 centers() 함수를 호출한 결과의 type은
        <class 'django.db.models.query.QuerySet'> 이다.
        """
        self.assertEqual(
            type(self.region_third_layer_0.centers()),
            QuerySet
        )
