from django.conf.urls import patterns, include, url
from task.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', group_list, name='group_list'),
    url(r'^login/$', login, name='login'),
    url(r'^loginin/$', loginin, name='loginin'),
    url(r'^login/success/', login_success, name='login_success'),
    url(r'^login/invalid/', login_invalid, name='login_invalid'),
    url(r'^group/(?P<name>\w+\W+\d+)', student_list, name='student_list'),
    url(r'^admin/', include(admin.site.urls)),
)
