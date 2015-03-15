from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns(
    '',

    # Django Default
    url(r'^admin/', include(admin.site.urls)),

    # Django 3rd Party Modules
    url('', include('social.apps.django_app.urls', namespace='social')),

    # Yebimom Urls
    url(r'^$', 'yebimom.views.home', name='home'),

    # Included Apps Urls
    url(r'^', include('events.urls', namespace='events', app_name='events')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
