# Views
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Models
from events.models import Event


class EventList(ListView):
    model = Event
    template_name = 'events/list.html'
    context_object_name = 'events'


class EventDetail(DetailView):
    model = Event
    template_name = 'events/detail.html'
    context_object_name = 'event'
