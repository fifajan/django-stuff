from django.conf.urls import patterns, url
from persons.views import index, list_persons, manage_persons

urlpatterns = [
    url(r'^$', index),

    url(r'^persons/$', list_persons),
    url(r'^manage/$', manage_persons),
]
