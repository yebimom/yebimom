from django.conf.urls import patterns, url
from centers import views

from centers.views import CenterList
from centers.views import CenterDetail

urlpatterns = patterns(
    '',

    url(r'^$', views.center, name='list'),
    url(r'^list/$', CenterList.as_view()),
    url(r'^(?P<slug>\w{5})/$', CenterDetail.as_view(), name='detail'),

    # Center registration
    url(r'^register/', views.center_register, name='register'),
    url(r'^register_complete/', views.center_register_complete, name='register_complete'),
)
