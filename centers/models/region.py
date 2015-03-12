from django.db import models

# Models
# from centers.models.center import Center


class RegionFirstLayerManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class RegionFirstLayer(models.Model):
    objects = RegionFirstLayerManager()

    name = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return unicode(self.name)

    def natural_key(self):
        return tuple([self.name])


class RegionSecondLayerManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class RegionSecondLayer(models.Model):
    objects = RegionSecondLayerManager()

    name = models.CharField(max_length=20, unique=True)
    region_first_layer = models.ForeignKey(RegionFirstLayer)

    def __unicode__(self):
        return u"%s %s" % (
            self.region_first_layer.name,
            self.name
        )

    def natural_key(self):
        return tuple([self.name])
    natural_key.dependencies = ['centers.regionfirstlayer']


class RegionThirdLayerManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class RegionThirdLayer(models.Model):
    objects = RegionThirdLayerManager()

    name = models.CharField(max_length=20, unique=True)
    region_second_layer = models.ForeignKey(RegionSecondLayer)

    def __unicode__(self):
        return u"%s %s %s" % (
            self.region_second_layer.region_first_layer.name,
            self.region_second_layer.name,
            self.name
        )

    def natural_key(self):
        return tuple([self.name])
    natural_key.dependencies = ['centers.regionsecondlayer']
