from __future__ import absolute_import

from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView

from events.models import Event
from api.serializers.events import EventSerializer


class EventList(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
