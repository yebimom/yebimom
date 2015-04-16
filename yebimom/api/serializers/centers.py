from __future__ import absolute_import

from rest_framework import serializers

from centers.models import Center


class CenterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Center
        fields = (
            'id',
            'name',
            'address',
            'phone',
            'url',
            'min_price',
            'max_price',
            'hash_id',
            'region_first_layer',
            'region_second_layer',
            'region_third_layer',
            'facility_set',
            'policy_set',
            'program_set',
            'main_image_url',
        )
