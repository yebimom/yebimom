from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap
from yebimom.sitemaps import sitemaps


urlpatterns = patterns(
    '',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^robots\.txt$', include('robots.urls')),

    # Django 3rd Party Modules
    url('', include('social.apps.django_app.urls', namespace='social')),

    # Yebimom Urls
    url(r'^$', 'yebimom.views.home', name='home'),

    # Rules ( Static Pages )
    url(r'^rules/service/$', 'yebimom.views.service', name='service'),
    url(r'^rules/privacy/$', 'yebimom.views.privacy', name='privacy'),
    url(r'^rules/disclaimer/$', 'yebimom.views.disclaimer', name='disclaimer'),
    url(r'^rules/search-policy/$', 'yebimom.views.search_policy', name='search_policy'),

    # Included Apps Urls
    url(r'^events/', include('events.urls', namespace='events', app_name='events')),
    url(r'^', include('users.urls', namespace='users', app_name='users')),
    url(r'^api/', include('api.urls', namespace='api', app_name='api')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
