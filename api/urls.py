from django.conf.urls import patterns, url

# Views
from api.views import EventList
from api.views import EventDetail
from api.views import CenterList
from api.views import CenterDetail

urlpatterns = patterns(
    '',

    # Event Urls
    url(r'^events/$', EventList.as_view(), name='list'),
    url(r'^events/(?P<pk>\d+)/$', EventDetail.as_view(), name='detail'),

    url(r'^centers/$', CenterList.as_view(), name='list'),
    url(r'^centers/(?P<pk>\d+)/$', CenterDetail.as_view(), name='detail'),
)
