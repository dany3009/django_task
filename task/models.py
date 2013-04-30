from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
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

class ModelSave(models.Model):
    name = models.CharField(max_length = 100)
    action = models.CharField(max_length = 100)
    time = models.DateField()

@receiver(post_save)
def post_save_handler(sender, **kwargs):
    from datetime import datetime 
    modelsave = ModelSave(name = sender.__name__, action = 'Save', time = datetime.now() )
    modelsave.save()

@receiver(post_delete)
def post_delete_handler(sender, **kwargs):
    from datetime import datetime 
    modelsave = ModelSave(name = sender.__name__, action = 'Delete', time = datetime.now() )
    modelsave.save()