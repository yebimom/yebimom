from rest_framework import serializers

# Models
from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:detail')
    homepage = serializers.HyperlinkedIdentityField(view_name='events:detail')

    class Meta:
        model = Event
        fields = ('id', 'title', 'contents', 'starts_at', 'ends_at', 'is_in_progress', 'thumbnail', 'url', 'homepage')
