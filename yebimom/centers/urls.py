from django.conf.urls import patterns, url

from centers.views import CenterList
from centers.views import CenterDetail

from centers.views import VisitReviewCreate
from centers.views import VisitReviewUpdate
from centers.views import VisitReviewDelete

from centers.views import UseReviewCreate
from centers.views import UseReviewUpdate
from centers.views import UseReviewDelete

urlpatterns = patterns(
    '',

    url(r'^$', CenterList.as_view(), name='list'),
    url(r'^(?P<slug>\w{5})/$', CenterDetail.as_view(), name='detail'),

    url(r'^(?P<slug>\w{5})/review/use/$', UseReviewCreate.as_view(), name='create_use_review'),
    url(r'^(?P<slug>\w{5})/review/use/update/$', UseReviewUpdate.as_view(), name='update_use_review'),
    url(r'^(?P<slug>\w{5})/review/use/delete/$', UseReviewDelete.as_view(), name='delete_use_review'),

    url(r'^(?P<slug>\w{5})/review/visit/$', VisitReviewCreate.as_view(), name='create_visit_review'),
    url(r'^(?P<slug>\w{5})/review/visit/update/$', VisitReviewUpdate.as_view(), name='update_visit_review'),
    url(r'^(?P<slug>\w{5})/review/visit/delete/$', VisitReviewDelete.as_view(), name='delete_visit_review'),
)