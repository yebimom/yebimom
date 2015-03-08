from django.conf.urls import patterns, url
from centers.views import upload_center_image


urlpatterns = patterns(
    '',

    # Center image file upload Url
    url(r'^upload/', upload_center_image.upload, name="upload"),
)
