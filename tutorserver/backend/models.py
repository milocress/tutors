from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
    name = models.CharField("name of subject", max_length=50)

    class Meta:
        unique_together = ['name']
        ordering = ['name']


class Student(models.Model):
    name = models.CharField("name of student", max_length=50)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='student')

    class Meta:
        unique_together = ['name']
        ordering = ['name']


class Tutor(models.Model):
    name = models.CharField("name of tutor", max_length=50)
    specialties = models.ManyToManyField(Subject,
                                         related_name="tutors")
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='tutor')

    class Meta:
        unique_together = ['name']
        ordering = ['name']


class TutorSession(models.Model):
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()

    tutor = models.ForeignKey(Tutor,
                              on_delete=models.CASCADE,
                              related_name='tutor_sessions')

    student = models.ForeignKey(Student,
                                on_delete=models.CASCADE,
                                related_name='student_sessions')


class SessionRequest(models.Model):
    date = models.DateTimeField(auto_now_add=True)

    subject = models.ForeignKey(Subject,
                                on_delete=models.CASCADE,
                                related_name='subject_session_requests')

    student = models.ForeignKey(Student,
                                on_delete=models.CASCADE,
                                related_name='student_session_requests')

    accepted_tutors = models.ManyToManyField(
        Tutor,
        related_name="accepted_sessions")

    active = models.BooleanField()
