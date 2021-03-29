from django.urls import path
from backend import views

urlpatterns = [
    path('', views.root_view),
    path('student/', views.student_view),
    path('tutor/', views.tutor_view),
]
