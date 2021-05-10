from rest_framework import serializers
from .models import Student, Tutor, TutorSession, SessionRequest, Subject
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'email', 'username'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = 'name', 'student_sessions', 'user'


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = 'name', 'tutor_sessions', 'accepted_sessions', 'specialties', 'user'


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorSession
        fields = 'tutor', 'student', 'start', 'end', 'rating'


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionRequest
        fields = 'date', 'subject', 'student', 'accepted_tutors', 'active'

