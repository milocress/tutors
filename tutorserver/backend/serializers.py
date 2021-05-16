from rest_framework import serializers
from .models import Student, Tutor, TutorSession, SessionRequest, Subject
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
        )

        return user

    class Meta:
        model = User
        fields = 'email', 'username', 'password'


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

