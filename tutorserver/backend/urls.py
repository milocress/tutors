from django.urls import path
from backend import views

urlpatterns = [
    path('', views.root_view),
    path('student/', views.student_view),
    path('tutor/', views.tutor_view),
    path('request/<int:rid>/', views.request_view),
    path('accept-request/<int:rid>', views.accept_request_view)
]
