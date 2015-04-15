from __future__ import absolute_import

from rest_framework import serializers

from users.models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        exclude = ('user', 'center')
