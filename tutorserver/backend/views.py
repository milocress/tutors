from django.http import HttpResponse

# from backend.models import # import models here

def student_view(request):
    return HttpResponse("Student view")

def tutor_view(request):
    return HttpResponse("Tutor view")

