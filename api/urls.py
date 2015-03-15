from django.conf.urls import patterns, url

# Views
from api.views import EventList
from api.views import EventDetail


urlpatterns = patterns(
    '',

    # Event Urls
    url(r'^events/$', EventList.as_view(), name='list'),
    url(r'^events/(?P<pk>\d+)/$', EventDetail.as_view(), name='detail'),
)
