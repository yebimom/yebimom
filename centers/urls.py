from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',

    # Center image file upload Url
    url(r'^upload/', 'centers.views.upload', name="upload"),
)
