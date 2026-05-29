from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.organization_dashboard, name='organization-dashboard'),
    path('settings/', views.organization_settings, name='organization-settings'),
    path('members/', views.organization_members, name='organization-members'),
    path('profile/', views.organization_profile, name='organization-profile'),
]
