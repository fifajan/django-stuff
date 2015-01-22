from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'app.views.index'),

    url(r'^persons/$', 'app.views.all_persons'),
    url(r'^manage/$', 'app.views.manage_persons'),

    url(r'^admin/', include(admin.site.urls)),
)
