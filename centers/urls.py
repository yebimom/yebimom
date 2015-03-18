from django.conf.urls import patterns, url
from centers import views

urlpatterns = patterns(
    '',

    url(r'^$', views.center, name='center'),

    # Center registration
    url(r'^register/', views.center_register, name='register'),
    url(r'^register_complete/', views.center_register_complete, name='register_complete'),
    # url(r'^detail/', views.center_detail, name='detail'),
    url(r'^(?P<hash_id>\w{5})/$', views.center_detail, name='detail'),
)
