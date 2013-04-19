from django.conf.urls import patterns, include, url
from task.views import group_list

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', group_list),
    url(r'^admin/', include(admin.site.urls)),
)
