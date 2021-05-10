from django.urls import path
from . import views

urlpatterns = [
    path('', views.root_view),
    path('student/', views.student_view),
    path('tutor/', views.tutor_view),
    path('request/<int:rid>/', views.request_view),
    path('accept-request/<int:rid>', views.accept_request_view),
    path('api/students', views.StudentListCreate.as_view()),
    path('api/sessions', views.SessionListCreate.as_view()),
    path('api/requests', views.RequestListCreate.as_view()),
    path('api/tutors',   views.TutorListCreate.as_view()),
    path('api/users', views.UserListCreate.as_view()),
]
