from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',

    url(r'^login/$', 'users.views.login_view', name='login'),
    url(r'^logout/$', 'users.views.logout_view', name='logout'),
    url(r'^signup/$', 'users.views.signup', name='signup'),
)
