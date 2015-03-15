from rest_framework import serializers

# Models
from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'contents', 'starts_at', 'ends_at')
