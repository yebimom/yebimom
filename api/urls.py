from django.conf.urls import patterns, url

# Views
from api.views.view_events import EventList
from api.views.view_events import EventDetail
from api.views.view_centers import CenterList
from api.views.view_centers import CenterDetail
from api.views.view_reviews import UserAllReviewList


urlpatterns = patterns(
    '',

    # Event Urls
    url(r'^events/$', EventList.as_view(), name='list'),
    url(r'^events/(?P<pk>\d+)/$', EventDetail.as_view(), name='detail'),

    url(r'^centers/$', CenterList.as_view(), name='list'),
    url(r'^centers/(?P<hash_id>\w{5})/$', CenterDetail.as_view(), name='detail'),

    url(r'^login/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^reviews/$', UserAllReviewList.as_view(), name='list'),
)
