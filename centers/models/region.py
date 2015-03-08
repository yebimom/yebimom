from django.db import models

# Models
# from centers.models.center import Center


class RegionFirstLayer(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return unicode(self.name)


class RegionSecondLayer(models.Model):
    name = models.CharField(max_length=20)
    region_first_layer = models.ForeignKey(RegionFirstLayer)

    def __unicode__(self):
        return u"%s %s" % (
            self.first_layer.name,
            self.name
        )


class RegionThirdLayer(models.Model):
    name = models.CharField(max_length=20)
    region_second_layer = models.ForeignKey(RegionSecondLayer)

    def __unicode__(self):
        return u"%s %s %s" % (
            self.second_layer.first_layer.name,
            self.second_layer.name,
            self.name
        )
