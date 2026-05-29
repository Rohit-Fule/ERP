from django.contrib import admin
from .models import Ticket, TicketResponse, SupportTeamMember, TicketRating


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_id', 'user', 'subject', 'category', 'priority', 'status', 'assigned_to', 'created_at')
    list_filter = ('status', 'priority', 'category', 'created_at')
    search_fields = ('ticket_id', 'subject', 'user__email', 'assigned_to__email')
    readonly_fields = ('ticket_id', 'created_at', 'updated_at', 'resolved_at')
    
    fieldsets = (
        ('Ticket Information', {
            'fields': ('ticket_id', 'user', 'subject', 'description')
        }),
        ('Classification', {
            'fields': ('category', 'priority', 'status')
        }),
        ('Assignment', {
            'fields': ('assigned_to',)
        }),
        ('Attachment', {
            'fields': ('attachment',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'resolved_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(TicketResponse)
class TicketResponseAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'responder', 'is_internal', 'created_at')
    list_filter = ('is_internal', 'created_at')
    search_fields = ('ticket__ticket_id', 'responder__email', 'message')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(SupportTeamMember)
class SupportTeamMemberAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'user', 'role', 'department', 'total_tickets_handled', 'average_rating', 'is_active')
    list_filter = ('role', 'is_active', 'created_at')
    search_fields = ('user__email', 'employee_id', 'user__first_name', 'user__last_name')
    readonly_fields = ('created_at', 'updated_at', 'total_tickets_handled', 'average_rating')


@admin.register(TicketRating)
class TicketRatingAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('ticket__ticket_id',)
