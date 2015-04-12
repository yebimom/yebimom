from django.contrib import sitemaps

from django.core.urlresolvers import reverse

# Models
from events.models import Event


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)


event_dict = {
    'queryset': Event.objects.all(),
    'date_field': 'starts_at',
}

sitemaps = {
    'static': StaticViewSitemap,
    'event': sitemaps.GenericSitemap(event_dict, priority=0.5),
}
