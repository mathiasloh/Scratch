from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', home, name='index'),
    url(r'^merlin/', home, name='index'),
    url(r'^pauline/', base , name='index'),
]
