from __future__ import absolute_import

from rest_framework import serializers

from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    api_url = serializers.HyperlinkedIdentityField(view_name='api:detail')
    web_url = serializers.HyperlinkedIdentityField(view_name='events:detail')

    class Meta:
        model = Event
        fields = (
            'id',
            'title',
            'contents',
            'starts_at',
            'ends_at',
            'is_in_progress',
            'thumbnail',
            'api_url',
            'web_url',
        )
