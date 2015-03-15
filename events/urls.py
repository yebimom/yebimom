from django.conf.urls import patterns, url
from events.views import EventDetailView


urlpatterns = patterns(
    '',

    # Event Urls
    url(r'^(?P<pk>\d+)/$', EventDetailView.as_view(), name='detail'),
)
