from django.views.generic.detail import DetailView
from events.models import Event


class EventDetailView(DetailView):
    model = Event
    template_name = 'events/detail.html'
