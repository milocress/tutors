from django.http import HttpResponse, HttpResponseRedirect

from .models import Student, Tutor, Subject, SessionRequest, TutorSession
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from rest_framework import generics
from .serializers import SessionSerializer, RequestSerializer, StudentSerializer, TutorSerializer

from .forms import SessionForm

# API Views:


class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TutorListCreate(generics.ListCreateAPIView):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer


class SessionListCreate(generics.ListCreateAPIView):
    queryset = TutorSession.objects.all()
    serializer_class = SessionSerializer


class RequestListCreate(generics.ListCreateAPIView):
    queryset = SessionRequest.objects.all()
    serializer_class = RequestSerializer


def root_view(request):
    print(Student.objects.all())
    return HttpResponse("Index page")


@login_required
def student_view(request):
    student = request.user.student.all()[0]

    if request.method == 'POST':
        form = SessionForm(request.POST)

        if form.is_valid():
            subject = Subject.objects.get(name=form.cleaned_data['subject'])
            sr = SessionRequest(subject=subject
                                , student=student
                                , active=True)
            sr.save()

            return HttpResponseRedirect(f'/request/{sr.pk}')

    else:
        form = SessionForm()

    past_sessions = student.student_sessions.all().values()

    active_requests = student.student_session_requests.all().values()
    return render(request, 'student_view.html',
                  {
                      'past_sessions': past_sessions,
                      'active_requests': active_requests,
                      'student': student,
                      'form': form
                  })


@login_required
def request_view(request, rid):
    req = SessionRequest.objects.get(pk=rid)

    return render(request, 'request_view.html',
                  {
                      'available_tutors': req.accepted_tutors.all(),
                      'price': 1
                  })


@login_required
def accept_request_view(request, rid):
    req = SessionRequest.objects.get(pk=rid)
    student = req.student.name
    subject = req.subject.name

    tutor = request.user.tutor.all()[0]

    req.accepted_tutors.add(tutor)

    return HttpResponse(f"{req}, requesting student={student}, subject={subject}")


@login_required
def tutor_view(request):
    response = HttpResponse(content_type="text/plain")
    tutor = request.user.tutor.all()[0]

    active_requests = SessionRequest.objects.all().values()

    return render(request, 'tutor_view.html',
                  {
                      'active_requests': active_requests,
                      'tutor': tutor
                  })
