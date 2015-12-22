from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'persons.views.index'),

    url(r'^persons/$', 'persons.views.list_persons'),
    url(r'^manage/$', 'persons.views.manage_persons'),
)
