from django.db import models
from django.contrib import admin

class Student(models.Model):
    name = models.CharField(max_length = 100)
    birth_date = models.DateField()
    ticket_number = models.IntegerField()
    group = models.CharField(max_length = 10)
    
    def __unicode__(self):
        return self.name
    
class Group(models.Model):
    name = models.CharField(max_length = 10)
    warden = models.ForeignKey('Student', related_name = 'student')
    
    def __unicode__(self):
        return self.name

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'group')
    
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'warden')
    
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
            query['sql'] = re.sub(r'(FROM|WHERE)', '\n\\1', query['sql'])
            query['sql'] = re.sub(r'((?:[^,]+,){3})', '\\1\n    ', query['sql'])
            
        res = '<p align="center">Query time: ' + str(query_time) + '<br />Query count: ' + str(query_count) + '</p></body>'    
        response.content = response.content.replace('</body>', res)
        return response
    
    
admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)