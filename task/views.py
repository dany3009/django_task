from django.template import loader, Context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from task.models import Student, Group
from django.contrib import auth

def group_list(request):
    groups = Group.objects.all()
    students = Student.objects.all()
    templ = loader.get_template('home.html')
    cont = Context({ 'groups' : groups, 'students' : students})
    return HttpResponse(templ.render(cont))

def student_list(request, name):
    students = Student.objects.all()
    list =[]
    
    for student in students:
        if (name == student.group):
            list.append(student)
            
    templ = loader.get_template('students.html')
    cont = Context({ 'list' : list })
    return HttpResponse(templ.render(cont))

def login(request):
    return render(request, 'login.html')

def login_success(request):
    templ = loader.get_template('status_login.html')
    cont = Context({ 'status' : 'Login Success' })
    return HttpResponse(templ.render(cont))

def login_invalid(request):
    templ = loader.get_template('status_login.html')
    cont = Context({ 'status' : 'Login Invalid' })
    return HttpResponse(templ.render(cont))

def loginin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/login/success/')
        else:
            return HttpResponseRedirect('/login/invalid/')
    else:
        pass