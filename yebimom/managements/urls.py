from django.conf.urls import patterns, url

from managements.views import ManagementDashboard


urlpatterns = patterns(
    '',

    url(r'^$', ManagementDashboard.as_view(), name='dashboard'),
)
