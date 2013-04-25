from django.db import models
from task.admin import *

class Student(models.Model):
    name = models.CharField(max_length = 100)
    birth_date = models.DateField()
    ticket_number = models.IntegerField()
    group = models.ForeignKey('Group', related_name = 'group')
    
    def __unicode__(self):
        return self.name
    
class Group(models.Model):
    name = models.CharField(max_length = 10)
    warden = models.ForeignKey('Student', related_name = 'warden')
    
    def get_student_count(self):
        return len(Student.objects.filter(group = self.id))
    
    def __unicode__(self):
        return self.name
    
class SqlRequests(object):
    def process_response(self, request, response):
        import re
        from django.db import connection
        queries = connection.queries
        query_time = 0
        query_count = 0
        for query in queries:
            query_time += float(query['time'])
            query_count += int(1)
            
        res = '<p align="center">Query time: ' + str(query_time) + '<br />Query count: ' + str(query_count) + '</p>\n</body>'    
        response.content = response.content.replace('</body>', res)
        return response

admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)