from django.conf.urls import patterns, url
from centers import views

urlpatterns = patterns(
    '',

    url(r'^center/$', views.center),

    # Center registration
    url(r'^center/register/', views.center_register, name='register'),
    url(r'^center/register_complete/', views.center_register_complete, name='register_complete'),
)
