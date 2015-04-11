from django.conf.urls import patterns, url

from users.views import MyPage


urlpatterns = patterns(
    '',

    url(r'^login/$', 'users.views.login_view', name='login'),
    url(r'^logout/$', 'users.views.logout_view', name='logout'),
    url(r'^signup/$', 'users.views.signup', name='signup'),

    url(r'^mypage/$', MyPage.as_view(), name='mypage'),
)
