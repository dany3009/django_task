from django.contrib import admin

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'group')
    
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'warden')