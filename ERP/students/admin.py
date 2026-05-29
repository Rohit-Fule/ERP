from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('enrollment_number', 'user', 'organization', 'program', 'semester', 'academic_status', 'current_gpa', 'created_at')
    list_filter = ('organization', 'academic_status', 'program', 'semester', 'created_at')
    search_fields = ('user__email', 'enrollment_number', 'user__first_name', 'user__last_name')
    readonly_fields = ('created_at', 'updated_at', 'total_courses_enrolled', 'total_courses_completed')
    
    fieldsets = (
        ('User Information', {
            'fields': ('user', 'organization')
        }),
        ('Enrollment Details', {
            'fields': ('enrollment_number', 'roll_number', 'enrollment_date')
        }),
        ('Academic Information', {
            'fields': ('program', 'semester', 'batch_year', 'expected_graduation_date')
        }),
        ('Academic Performance', {
            'fields': ('academic_status', 'current_gpa', 'total_courses_enrolled', 'total_courses_completed'),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
