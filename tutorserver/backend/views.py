from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt

from .models import Student, Tutor, Subject, SessionRequest, TutorSession
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import viewsets, response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .serializers import \
    SessionSerializer, RequestSerializer, StudentSerializer, \
    TutorSerializer, UserSerializer, SubjectSerializer

from .forms import SessionForm

from datetime import datetime

# Utility Functions:


def is_tutor(request):
    return list(request.user.tutor)

# API Views:


class UserViewSet(viewsets.ModelViewSet):
    def get_permissions(self):
        if self.action == 'create':
            my_permission_classes = []
        else:
            my_permission_classes = [IsAuthenticated]

        return [permission() for permission in my_permission_classes]

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
        # istutor = is_tutor(request)
        queryset = SessionRequest.objects.all()

        # if istutor:
        #     tutor = istutor[0]
        #     specialties = tutor.specialties
        #     queryset = SessionRequest.objects.filter(subject__in=specialties)

        serializer = RequestSerializer(queryset, many=True)
        return response.Response(serializer.data)

    def create(self, request, *args, **kwargs):
        subject, _ = Subject.objects.get_or_create(name=request.data['subject'])
        student = Student.objects.get(pk=request.data['student'])
        my_request = SessionRequest.objects.create(description=request.data['description'],
                                                   student=student, active=request.data['active'],
                                                   subject=subject)

        my_request.save()

        serializer = RequestSerializer(my_request)
        return response.Response(serializer.data)


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]


@permission_classes([IsAuthenticated])
def current_user_view(request):
    user = request.user
    print(user)
    serializer = UserSerializer(user)
    return JsonResponse(serializer.data)


@permission_classes([IsAuthenticated])
def get_user_by_username(request, username):
    user = User.objects.get_by_natural_key(username)
    serializer = UserSerializer(user)
    return JsonResponse(serializer.data)


@csrf_exempt
def accept(request, rid, tid):
    request = SessionRequest.objects.get(pk=rid)
    tutor = Tutor.objects.get(pk=tid)
    request.accepted_tutors.add(tutor)
    request.save()
    session = TutorSession(student=request.student, tutor=tutor, request=request, rating=-1)
    session.save()
    serializer = SessionSerializer(session)
    return JsonResponse(serializer.data)


@csrf_exempt
def end_session(request, sid):
    session = TutorSession.objects.get(pk=sid)
    session.end = datetime.utcnow()
    session.save()

    naive = session.start.replace(tzinfo=None)

    delta = session.end - naive

    session.student.amount_owed += delta.total_seconds()
    session.student.save()

    serializer = SessionSerializer(session)
    return JsonResponse(serializer.data)


@csrf_exempt
def clear_balance(request, sid):
    student = Student.objects.get(pk=sid)
    student.amount_owed = 0
    student.save()
    return HttpResponse(status=200)


def root_view(request):
    return render("Index page")


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
