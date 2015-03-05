from django.db import models

# Models
from centers.models.center import Center


class RegionFirstLayer(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return unicode(self.name)

    def centers(self):
        region_second_layer_set = self.regionsecondlayer_set.all()

        region_third_layer_set = list()
        for region_second_layer in region_second_layer_set:
            region_third_layer_set.extend(
                region_second_layer.regionthirdlayer_set.all()
            )

        centers =  Center.objects.filter(
            region__in=region_third_layer_set
        )
        return centers


class RegionSecondLayer(models.Model):
    name = models.CharField(max_length=20)
    first_layer = models.ForeignKey(RegionFirstLayer)

    def __unicode__(self):
        return u"%s %s" % (
            self.first_layer.name,
            self.name
        )

    def centers(self):
        region_third_layer_set = self.regionthirdlayer_set.all()
        centers =  Center.objects.filter(
            region__in=region_third_layer_set
        )
        return centers


class RegionThirdLayer(models.Model):
    name = models.CharField(max_length=20)
    second_layer = models.ForeignKey(RegionSecondLayer)

    def __unicode__(self):
        return u"%s %s %s" % (
            self.second_layer.first_layer.name,
            self.second_layer.name,
            self.name
        )

    def centers(self):
        return self.center_set.all()
