# Command
from django.core.management.base import BaseCommand, CommandError

# Models
from centers.models.region import RegionFirstLayer
from centers.models.region import RegionSecondLayer
from centers.models.region import RegionThirdLayer

# Data
from centers.management.commands._regions import REGIONS


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
                    "<RegionSecondLayer: %s %s>" %
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
                        "<RegionSecondLayer: %s %s %s>" %
                        (
                            region_first_layer["name"].decode('utf-8'),
                            region_second_layer["name"].decode('utf-8'),
                            region_third_layer["name"].decode('utf-8')
                        )
                    )
