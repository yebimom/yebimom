from django.conf.urls import patterns, url

# Views
from api.views.events import EventList, EventDetail
from api.views.centers import CenterList, CenterDetail
from api.views.regions import RegionList
from api.views.reviews import UserVisitReviewList, UserUseReviewList
from api.views.reviews import CreateVisitReview, UpdateVisitReview, DeleteVisitReview
from api.views.reviews import CreateUseReview, UpdateUseReview, DeleteUseReview


urlpatterns = patterns(
    '',

    url(r'^login/', 'rest_framework_jwt.views.obtain_jwt_token'),

    url(r'^events/$', EventList.as_view(), name='events_list'),
    url(r'^events/(?P<pk>\d+)/$', EventDetail.as_view(), name='event_detail'),

    url(r'^centers/$', CenterList.as_view(), name='centers_list'),
    url(r'^centers/(?P<hash_id>\w{5})/$', CenterDetail.as_view(), name='center_detail'),

    url(r'^regions/$', RegionList.as_view(), name='regions_list'),

    url(r'^users/reviews/visit/$', UserVisitReviewList.as_view(), name='visit_reviews'),
    url(r'^users/reviews/use/$', UserUseReviewList.as_view(), name='use_reviews'),

    url(r'^centers/(?P<hash_id>\w{5})/reviews/visit/$', CreateVisitReview.as_view(), name='create_visit_review'),
    url(r'^centers/(?P<hash_id>\w{5})/reviews/visit/update/$', UpdateVisitReview.as_view(), name='update_visit_review'),
    url(r'^centers/(?P<hash_id>\w{5})/reviews/visit/delete/$', DeleteVisitReview.as_view(), name='delete_visit_review'),

    url(r'^centers/(?P<hash_id>\w{5})/reviews/use/$', CreateUseReview.as_view(), name='create_use_review'),
    url(r'^centers/(?P<hash_id>\w{5})/reviews/use/update/$', UpdateUseReview.as_view(), name='update_use_review'),
    url(r'^centers/(?P<hash_id>\w{5})/reviews/use/delete/$', DeleteUseReview.as_view(), name='delete_use_review'),
)
