from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'persons.views.index'),

    url(r'^persons/$', 'persons.views.list_persons'),
    url(r'^manage/$', 'persons.views.manage_persons'),

    url(r'^admin/', include(admin.site.urls)),
)
