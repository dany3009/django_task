from django.conf.urls import patterns, include, url
from task.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', group_list),
    url(r'^login/$', login),
    url(r'^group/(?P<name>\w+\W+\d+)', student_list),
    url(r'^admin/', include(admin.site.urls)),
)
