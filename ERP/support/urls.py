from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.support_dashboard, name='support-dashboard'),
    path('tickets/', views.ticket_list, name='support-ticket-list'),
    path('ticket/<str:ticket_id>/', views.ticket_detail, name='support-ticket-detail'),
    path('create/', views.create_ticket, name='create-ticket'),
    path('my-tickets/', views.my_tickets, name='my-tickets'),
    path('my-tickets/<str:ticket_id>/', views.view_ticket, name='support-view-ticket'),
    path('profile/edit/', views.support_profile_edit, name='support-profile-edit'),
]
