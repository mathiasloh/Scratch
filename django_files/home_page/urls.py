from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', home, name='index'),
    url(r'^users/(?P<username>[\w.@+-]+)/$', home_user, name = 'user_index'),
  	url(r'^users/(?P<username>[\w.@+-]+)/play/$', play_user, name = 'user_play'),
  	url(r'^users/(?P<username>[\w.@+-]+)/tutorial/$', tuto_user, name='user_tuto'),
  	url(r'^users/(?P<username>[\w.@+-]+)/summary/$', summary_user, name='user_summary'),
]
