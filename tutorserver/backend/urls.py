from django.urls import path, include
from rest_framework.authtoken import views as auth_views
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r'users', views.UserViewSet, basename='users')
router.register(r'students', views.StudentViewSet, basename='students')
router.register(r'tutors', views.TutorViewSet, basename='tutors')
router.register(r'sessions', views.SessionViewSet, basename='sessions')
router.register(r'requests', views.RequestViewSet, basename='requests')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/current-user/', views.current_user_view),
    path('api/username/<str:username>/', views.get_user_by_username),
    path('api/token-auth/', auth_views.obtain_auth_token),
    path('api/accept/<int:rid>/<int:tid>', views.accept),
    path('api/end_session/<int:sid>', views.end_session),
    path('api/clear_balance/<int:sid>', views.clear_balance),
    path('api/rate/<int:sid>/<int:rating>', views.rate),
    path('api/past_sessions/<int:sid>', views.past_sessions),
    # path('api/students', views.StudentListCreate.as_view()),
    # path('api/sessions', views.SessionListCreate.as_view()),
    # path('api/requests', views.RequestListCreate.as_view()),
    # path('api/tutors',   views.TutorListCreate.as_view()),
    # path('api/users', views.UserListCreate.as_view()),

    # Non-token-based authentication
    # path('api-auth/', include('rest_framework.urls')),

    # Non-api views
    path('', views.root_view),
    # path('student/', views.student_view),
    # path('tutor/', views.tutor_view),
    # path('request/<int:rid>/', views.request_view),
    # path('accept-request/<int:rid>', views.accept_request_view),
]
