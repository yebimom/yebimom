from django.views.generic.detail import DetailView
from events.models import Event


class EventDetail(DetailView):
    model = Event
    template_name = 'events/detail.html'
    context_object_name = 'event'
