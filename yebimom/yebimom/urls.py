from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap
from yebimom.sitemaps import sitemaps

from yebimom.views import Home
from centers.views import CategoryList, CategoryDetail
from centers.views import CenterLanding


urlpatterns = patterns(
    '',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^robots\.txt$', include('robots.urls')),

    # Django 3rd Party Modules
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^grappelli/', include('grappelli.urls')),

    # Yebimom Urls
    url(r'^$', Home.as_view(), name='home'),

    # Rules ( Static Pages )
    url(r'^rules/service/$', 'yebimom.views.service', name='service'),
    url(r'^rules/privacy/$', 'yebimom.views.privacy', name='privacy'),
    url(r'^rules/disclaimer/$', 'yebimom.views.disclaimer', name='disclaimer'),
    url(r'^rules/search-policy/$', 'yebimom.views.search_policy', name='search_policy'),

    # Included Apps Urls
    url(r'^centers/', include('centers.urls', namespace='centers')),
    url(r'^events/', include('events.urls', namespace='events')),
    url(r'^', include('users.urls', namespace='users')),
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^manage/', include('managements.urls', namespace='managements')),

    url(r'^category/$', CategoryList.as_view(), name='category-list'),
    url(r'^category/(?P<slug>\w+)/$', CategoryDetail.as_view(), name='category-detail'),

    # I18n ( Set language dynamically )
    url(r'^i18n/', include('django.conf.urls.i18n')),

    # Translation
    url(r'^rosetta/', include('rosetta.urls')),

    # Landing
    url(r'^(?P<slug>\w+)/landing/$', CenterLanding.as_view(), name='landing'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
