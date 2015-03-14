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

    url(r'^login/', 'users.views.login_view', name='login'),
    url(r'^logout/', 'users.views.logout_view', name='logout'),
)
