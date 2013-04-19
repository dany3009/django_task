from django.template import loader, Context
from django.http import HttpResponse
from task.models import Student, Group

def group_list(request):
    groups = Group.objects.all()
    students = Student.objects.all()
    templ = loader.get_template('home.html')
    cont = Context({ 'groups' : groups, 'students' : students})
    return HttpResponse(templ.render(cont))