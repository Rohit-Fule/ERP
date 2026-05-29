from django.urls import path
from . import views

urlpatterns = [
    # Generic login/register
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    
    # Student routes
    path('student/login/', views.student_login, name='student-login'),
    path('student/register/', views.student_register, name='student-register'),
    
    # Teacher routes
    path('teacher/login/', views.teacher_login, name='teacher-login'),
    path('teacher/register/', views.teacher_register, name='teacher-register'),
    
    # Organization routes
    path('organization/login/', views.organization_login, name='organization-login'),
    path('organization/register/', views.organization_register, name='organization-register'),
    
    # Support routes
    path('support/login/', views.support_login, name='support-login'),
    path('support/register/', views.support_register, name='support-register'),
]
