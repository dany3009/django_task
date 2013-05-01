from django.db import models
from task.admin import *
from task.signals import *

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
    
admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)