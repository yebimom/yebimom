from __future__ import absolute_import

from rest_framework import serializers

from centers.models import RegionThirdLayer


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegionThirdLayer
