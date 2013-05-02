from django.conf.urls import patterns, include, url
from task.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', group_list, name='group_list'),    
    url( r'^login/$', 'django.contrib.auth.views.login', { "template_name": "login.html" }, name='login'),
    url( r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    
    url(r'^student/(?P<student_id>\d+)/edit/', 'task.views.edit_student', name='edit_student'),
    url(r'^student/(?P<student_id>\d+)/delete/', 'task.views.delete_student', name='delete_student'),
    
    url(r'^group/(?P<group_id>\d+)/edit/', 'task.views.edit_group', name='edit_group'),
    url(r'^group/(?P<group_id>\d+)/delete/', 'task.views.delete_group', name='delete_group'),
    
    url(r'^group/(?P<name>\w+\W+\d+)', student_list, name='student_list'),
    url(r'^admin/', include(admin.site.urls)),
)
