from django.db import models


class RegionFirstLayer(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return unicode(self.name)


class RegionSecondLayer(models.Model):
    name = models.CharField(max_length=20)
    first_layer = models.ForeignKey(RegionFirstLayer)

    def __unicode__(self):
        return u"%s %s" % (
            self.first_layer.name,
            self.name
        )

    def centers(self):
        centers = list()
        region_third_layer_set = self.regionthirdlayer_set.all()

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
