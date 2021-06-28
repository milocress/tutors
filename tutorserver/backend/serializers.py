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

        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']

        user.save()
        return user

    class Meta:
        model = User
        fields = 'email', 'username', 'password', 'student', 'tutor', 'pk', 'first_name', 'last_name'
        depth = 1


class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'username', 'student', 'tutor', 'pk', 'first_name', 'last_name'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = 'student_sessions', 'user', 'pk'
        depth = 1


class StudentPublicSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer()

    class Meta:
        model = Student
        fields = '__all__'


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = 'tutor_sessions', 'accepted_sessions', 'specialties', 'user', 'pk'
        depth = 1


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorSession
        fields = 'tutor', 'student', 'start', 'end', 'rating', 'pk'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = 'name'


class RequestSerializer(serializers.ModelSerializer):
    student = StudentPublicSerializer()

    class Meta:
        model = SessionRequest
        fields = '__all__'
        depth = 1
