from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',

    # Django Default
    url(r'^admin/', include(admin.site.urls)),

    # Django 3rd Party Modules
    url('', include('social.apps.django_app.urls', namespace='social')),

    # Yebimom Urls
    url(r'^$', 'yebimom.views.home', name='home'),

    # Login, Logout
    url(r'^login/$', 'users.views.login_view', name='login'),
    url(r'^logout/$', 'users.views.logout_view', name='logout'),
    url(r'^signup/$', 'users.views.signup', name='signup'),

    # Rules ( Static Pages )
    url(r'^rules/service/$', 'yebimom.views.service', name='service'),
    url(r'^rules/privacy/$', 'yebimom.views.privacy', name='privacy'),
    url(r'^rules/disclaimer/$', 'yebimom.views.disclaimer', name='disclaimer'),
    url(r'^rules/search_policy/$', 'yebimom.views.search_policy', name='search_policy'),
)
