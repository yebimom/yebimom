from django.conf.urls import patterns, url

# Views
from api.views.events import EventList, EventDetail
from api.views.centers import CenterList, CenterDetail
from api.views.regions import RegionList
from api.views import reviews
from api.views.reviews import UserReviewList


urlpatterns = patterns(
    '',

    url(r'^login/', 'rest_framework_jwt.views.obtain_jwt_token'),

    url(r'^events/$', EventList.as_view(), name='list'),
    url(r'^events/(?P<pk>\d+)/$', EventDetail.as_view(), name='detail'),

    url(r'^centers/$', CenterList.as_view(), name='list'),
    url(r'^centers/(?P<hash_id>\w{5})/$', CenterDetail.as_view(), name='detail'),

    url(r'^regions/$', RegionList.as_view(), name='list'),

    url(r'^reviews/$', UserReviewList.as_view(), name='list'),

    # visited review
    url(r'^center/(?P<hash_id>\w{5})/reviews/visit/$',
        reviews.CreateReview.as_view(),
        name='create_visit_review'),

    url(r'^center/(?P<hash_id>\w{5})/reviews/visit/update/$',
        reviews.RetrieveUpdateDestroyReview.as_view(),
        name='update_visit_review'),

    url(r'^center/(?P<hash_id>\w{5})/reviews/visit/delete/$',
        reviews.RetrieveUpdateDestroyReview.as_view(),
        name='delete_visit_delete'),
)
