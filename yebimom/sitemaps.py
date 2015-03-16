from django.contrib.sitemaps import GenericSitemap

from events.models import Event


info_dict = {
    'queryset': Event.objects.all(),
    'date_field': 'starts_at',
}

sitemaps = {
    'event': GenericSitemap(info_dict, priority=0.6),
}
