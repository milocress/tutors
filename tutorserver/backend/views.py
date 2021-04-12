from django.http import HttpResponse

from backend.models import Student, Tutor, Subject, SessionRequest
from django.contrib.auth.decorators import login_required

def root_view(request):
    print(Student.objects.all())
    return HttpResponse("Index page")

@login_required
def student_view(request):
    response = HttpResponse(content_type="text/plain")
    default_student = Student.objects.get(name="Milo Cress")
    default_subject = Subject.objects.get(name="Default Subject")

    response.write('Student view \n')

    response.write('<h1>Sessions</h1> \n')
    response.write(str(default_student.student_sessions.all().values()) + '\n')
    response.write('<h1>New Session</h1> \n')
    response.write('<button>Request</button> \n')
    return response

@login_required
def tutor_view(request):
    response = HttpResponse(content_type="text/plain")
    default_tutor = Tutor.objects.get(name="Teddy Schoenfeld")

    response.write('Tutor view \n')
    response.write('<h1>Past Sessions</h1> \n')
    response.write(str(default_tutor.tutor_sessions.all().values()) + '\n')
    response.write('<h1>Available Sessions</h1> \n')
    response.write(str(SessionRequest.objects.all().values()) + '\n')
    
    return response

