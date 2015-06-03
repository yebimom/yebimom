from django.conf.urls import patterns, url

from managements.views import ManagementDashboard, ManagementCenterLanding


urlpatterns = patterns(
    '',

    url(r'^$', ManagementDashboard.as_view(), name='dashboard'),
    url(r'^center/(?P<slug>\w+)/landing/$', ManagementCenterLanding.as_view(), name='landing-list'),
)
