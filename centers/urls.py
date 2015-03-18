from django.conf.urls import patterns, url
from centers import views

urlpatterns = patterns(
    '',

    url(r'^$', views.center, name='center'),

    # Center registration
    url(r'^register/', views.center_register, name='register'),
    url(r'^register_complete/', views.center_register_complete, name='register_complete'),
)
