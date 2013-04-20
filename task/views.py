from django.template import loader, Context
from django.http import HttpResponse
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
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Invalid Login')
    else:
        return HttpResponse('Invalid Login')