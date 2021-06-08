from django.http import HttpResponse, HttpResponseRedirect

from .models import Student, Tutor, Subject, SessionRequest, TutorSession
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import viewsets, response
from rest_framework.permissions import IsAuthenticated
from .serializers import SessionSerializer, RequestSerializer, StudentSerializer, TutorSerializer, UserSerializer

from .forms import SessionForm

# Utility Functions:


def is_tutor(request):
    return list(request.user.tutor)

# API Views:


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]


class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
    permission_classes = [IsAuthenticated]


class SessionViewSet(viewsets.ModelViewSet):
    queryset = TutorSession.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [IsAuthenticated]


class RequestViewSet(viewsets.ModelViewSet):
    queryset = SessionRequest.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        istutor = is_tutor(request)
        queryset = SessionRequest.objects.all()

        if istutor:
            tutor = istutor[0]
            specialties = tutor.specialties
            queryset = SessionRequest.objects.filter(subject__in=specialties)

        serializer = RequestSerializer(queryset, many=True)
        return response.Response(serializer.data)


def root_view(request):
    print(Student.objects.all())
    return HttpResponse("Index page")


# Regular views

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
