from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.teacher_dashboard, name='teacher-dashboard'),
    path('courses/', views.teacher_courses, name='teacher-courses'),
    path('course/<int:course_id>/students/', views.course_students, name='course-students'),
    path('course/<int:course_id>/assignment/create/', views.create_assignment, name='create-assignment'),
    path('profile/', views.teacher_profile, name='teacher-profile'),
    path('profile/edit/', views.teacher_profile_edit, name='teacher-profile-edit'),
]
