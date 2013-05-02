from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from task.models import Student, Group
from task.forms import *

def group_list(request):
    groups = Group.objects.all()
    return direct_to_template(request, 'home.html', { 'groups' : groups})

def student_list(request, name):
    students = Student.objects.filter(group__name = name)
    return direct_to_template(request, 'students.html', { 'students' : students })

@login_required
def edit_student(request, student_id):
    student = get_object_or_404(Student.objects, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance = student)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
    return render(request, 'edit_student.html')
        
@login_required
def delete_student(request, student_id):
    student = get_object_or_404(Student, id = student_id)
    student.delete()
    return HttpResponseRedirect("/")

@login_required
def edit_group(request, group_id):
    studgroup = get_object_or_404(Group.objects, id = group_id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance = studgroup)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
    return render(request, 'edit_student.html')


@login_required
def delete_group(request, group_id):
    group = get_object_or_404(Group, id = group_id)
    group.delete()
    return HttpResponseRedirect("/") 