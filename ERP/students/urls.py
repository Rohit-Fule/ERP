from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.student_dashboard, name='student-dashboard'),
    path('courses/', views.student_courses, name='student-courses'),
    path('assignments/', views.student_assignments, name='student-assignments'),
    path('assignment/<int:assignment_id>/', views.assignment_detail, name='assignment-detail'),
    path('profile/', views.student_profile, name='student-profile'),
    path('profile/edit/', views.student_profile_edit, name='student-profile-edit'),
]
