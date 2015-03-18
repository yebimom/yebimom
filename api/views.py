from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView

from events.models import Event
from events.serializers import EventSerializer

from centers.models import Center
from centers.serializers import CenterSerializer


class EventList(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class CenterList(ListAPIView):
    queryset = Center.objects.all()
    serializer_class = CenterSerializer


class CenterDetail(RetrieveAPIView):
    queryset = Center.objects.all()
    serializer_class = CenterSerializer
