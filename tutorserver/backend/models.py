from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Subject(models.Model):
    name = models.CharField("name of subject", max_length=50)

    class Meta:
        unique_together = ['name']
        ordering = ['name']


class Student(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='student')

    amount_owed = models.FloatField(default=0)

    class Meta:
        unique_together = ['user']
        ordering = ['user']


class Tutor(models.Model):
    specialties = models.ManyToManyField(Subject,
                                         related_name="tutors")
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='tutor')

    class Meta:
        unique_together = ['user']
        ordering = ['user']


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

    description = models.CharField('symptom description', max_length=200)


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

    request = models.ForeignKey(SessionRequest,
                                on_delete=models.CASCADE,
                                related_name='session')
