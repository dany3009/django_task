from django.core.management.base import AppCommand
from task.models import Student, Group

class Command(AppCommand):
    requires_model_validation = True

    def handle_app(self, app, **options):
        groups = Group.objects.all()
        lines = []
        
        for group in groups:
            lines.append("[%s]\n" % group.name)
            for student in Student.objects.filter(group = group.id):
                lines.append("\t[%s]\n" % student.name)

        return "\n".join(lines)