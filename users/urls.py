from django.conf.urls import patterns, url

from users.views import Dashboard


urlpatterns = patterns(
    '',

    url(r'^login/$', 'users.views.login_view', name='login'),
    url(r'^logout/$', 'users.views.logout_view', name='logout'),
    url(r'^signup/$', 'users.views.signup', name='signup'),
    url(r'^contact/$', 'users.views.contact', name='contact'),
    url(r'^dashboard/$', Dashboard.as_view(), name='dashboard'),
)
