from rest_framework import serializers
from .models import Student, Tutor, TutorSession, SessionRequest, Subject


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = 'name', 'student_sessions'


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = 'name', 'tutor_sessions', 'accepted_sessions', 'specialties'


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorSession
        fields = 'tutor', 'student', 'start', 'end', 'rating'


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionRequest
        fields = 'date', 'subject', 'student', 'accepted_tutors', 'active'

