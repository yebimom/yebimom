from django.conf.urls import patterns, url

from centers.views import CenterList
from centers.views import CenterDetail
from centers.views import VisitReviewCreate
from centers.views import VisitReviewUpdate
from centers.views import VisitReviewDelete

urlpatterns = patterns(
    '',

    url(r'^$', CenterList.as_view(), name='list'),
    url(r'^(?P<slug>\w{5})/$', CenterDetail.as_view(), name='detail'),

    url(r'^(?P<slug>\w{5})/review/visit/$', VisitReviewCreate.as_view(), name='create_visit_review'),
    url(r'^(?P<slug>\w{5})/review/visit/update/$', VisitReviewUpdate.as_view(), name='update_visit_review'),
    url(r'^(?P<slug>\w{5})/review/visit/delete/$', VisitReviewDelete.as_view(), name='delete_visit_review'),
)
