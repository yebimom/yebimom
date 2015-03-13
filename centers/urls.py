from django.conf.urls import patterns, url
from centers import views

urlpatterns = patterns(
    '',

    url(r'^center/$', views.center),

    # Center registration
    url(r'^center/register/', views.center_registration),
)
