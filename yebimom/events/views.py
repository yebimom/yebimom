# Views
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Models
from events.models import Event
from centers.models.region import RegionSecondLayer, RegionThirdLayer


class EventList(ListView):
    queryset = Event.objects.order_by('-ends_at')
    template_name = 'events/list.html'
    context_object_name = 'events'

    def get_context_data(self, **kwargs):
        context = super(EventList, self).get_context_data(**kwargs)

        context['regions_second_layer'] = RegionSecondLayer.objects.all()
        context['regions_third_layer'] = RegionThirdLayer.objects.all()

        return context


class EventDetail(DetailView):
    model = Event
    template_name = 'events/detail.html'
    context_object_name = 'event'
