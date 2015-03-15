from django.conf.urls import patterns, url

# Views
from events.views import EventDetail


urlpatterns = patterns(
    '',

    # Event Urls
    url(r'^event/(?P<pk>\d+)/$', EventDetail.as_view(), name='detail'),
)
