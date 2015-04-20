from __future__ import absolute_import

from rest_framework import serializers

from centers.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = (
            'centers',
        )
