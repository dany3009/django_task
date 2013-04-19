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
    
admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)