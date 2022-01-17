from rest_framework import serializers
from .models import Student, Tutor, TutorSession, SessionRequest, Subject, Invite
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
        )

        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']

        user.save()

        student = Student(user=user)
        tutor = Tutor(user=user)
        student.save()
        tutor.save()

        return user

    class Meta:
        model = User
        fields = 'email', 'username', 'password', 'student', 'tutor', 'pk', 'first_name', 'last_name'
        depth = 1


class InviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invite
        fields = 'key', 'is_active'


class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'username', 'student', 'tutor', 'pk', 'first_name', 'last_name'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = 'student_sessions', 'user', 'pk', 'amount_owed'
        depth = 1


class StudentPublicSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer()

    class Meta:
        model = Student
        fields = 'user', 'pk'


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = 'tutor_sessions', 'accepted_sessions', 'specialties', 'user', 'pk'
        depth = 1


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorSession
        fields = 'tutor', 'student', 'start', 'end', 'rating', 'pk', 'id', 'request', 'report'
        depth = 1


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = 'name'


class RequestSerializer(serializers.ModelSerializer):
    student = StudentPublicSerializer()

    class Meta:
        model = SessionRequest
        fields = 'subject', 'student', 'date', 'accepted_tutors', 'session', 'description', 'active', 'pk', 'id'
        depth = 1
