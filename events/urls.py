from django.conf.urls import patterns, url

# Views
from events.views import EventList
from events.views import EventDetail


urlpatterns = patterns(
    '',

    # Event Urls
    url(r'^$', EventList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', EventDetail.as_view(), name='detail'),
)
