from django.conf.urls import patterns, url

from centers.views import CenterList
from centers.views import CenterDetail
from centers.views import ReviewCreate

urlpatterns = patterns(
    '',

    url(r'^$', CenterList.as_view(), name='list'),
    url(r'^(?P<slug>\w{5})/$', CenterDetail.as_view(), name='detail'),

    url(r'^(?P<slug>\w{5})/review/$', ReviewCreate.as_view(), name='create_review'),
    # url(r'^(?P<slug>\w{5})/review/edit/$', ReviewUpdate.as_view(), name='update_review'),
    # url(r'^(?P<slug>\w{5})/review/delete/$', ReviewDelete.as_view(), name='delete_review'),
)
