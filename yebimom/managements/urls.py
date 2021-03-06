from django.conf.urls import patterns, url

from managements.views import ManagementDashboard, ManagementCenterDashboard,\
    ManagementCenterLanding, ManagementCenterLandingDetail


urlpatterns = patterns(
    '',
    url(r'^$',
        ManagementDashboard.as_view(),
        name='dashboard'),
    url(r'^center/(?P<hash_id>\w+)/$',
        ManagementCenterDashboard.as_view(),
        name='center'),
    url(r'^center/(?P<hash_id>\w+)/landing/$',
        ManagementCenterLanding.as_view(),
        name='landing-list'),
    url(r'^center/(?P<hash_id>\w+)/landing/(?P<center_landing_hash_id>\w+)/$',
        ManagementCenterLandingDetail.as_view(),
        name='landing-detail'),
)
