# -*- coding: utf-8 -*-

# Command
from django.core.management.base import BaseCommand, CommandError

# Models
from centers.models.region import RegionFirstLayer
from centers.models.region import RegionSecondLayer
from centers.models.region import RegionThirdLayer

REGIONS = [
    {
        "name": "전국/서울",
        "region_second_layers": [
            {
                "name": "전국전체",
                "region_third_layers": [
                    {
                        "name": "강남/논현/반포",
                    },
                    {
                        "name": "삼성/선릉/역삼",
                    },
                    {
                        "name": "압구정/청담/신사",
                    }
                ]
            },
            {
                "name": "서울전체",
                "region_third_layers": [
                ]
            }
        ]
    },
    {
        "name": "인천/경기",
        "region_second_layers": [
        ]
    },
    {
        "name": "대구/부산",
        "region_second_layers": [
        ]
    }
]


class Command(BaseCommand):
    help = 'Initialize Regions Fixtures'

    def handle(self, *args, **options):
        for region_first_layer in REGIONS:
            region_first_layer_object = RegionFirstLayer.objects.create(
                name=region_first_layer["name"]
            )
            self.stdout.write("<RegionFirstLayer: %s>" % region_first_layer["name"].decode('utf-8'))

            for region_second_layer in region_first_layer["region_second_layers"]:
                region_second_layer_object = RegionSecondLayer.objects.create(
                    region_first_layer=region_first_layer_object,
                    name=region_second_layer["name"]
                )
                self.stdout.write(
                    "<RegionSecondLayer: %s %s>" % \
                    (
                        region_first_layer["name"].decode('utf-8'),
                        region_second_layer["name"].decode('utf-8')
                    )
                )

                for region_third_layer in region_second_layer["region_third_layers"]:
                    region_third_layer_object = RegionThirdLayer.objects.create(
                        region_second_layer=region_second_layer_object,
                        name=region_third_layer["name"]
                    )
                    self.stdout.write(
                        "<RegionSecondLayer: %s %s %s>" % \
                        (
                            region_first_layer["name"].decode('utf-8'),
                            region_second_layer["name"].decode('utf-8'),
                            region_third_layer["name"].decode('utf-8')
                        )
                    )
