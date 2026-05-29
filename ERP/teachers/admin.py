from django.contrib import admin
from .models import Teacher, TeacherQualification


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'user', 'organization', 'designation', 'department', 'total_courses', 'is_active', 'created_at')
    list_filter = ('organization', 'is_active', 'qualification', 'created_at')
    search_fields = ('user__email', 'employee_id', 'user__first_name', 'user__last_name')
    readonly_fields = ('created_at', 'updated_at', 'total_courses', 'total_students')
    
    fieldsets = (
        ('User Information', {
            'fields': ('user', 'organization')
        }),
        ('Employment Details', {
            'fields': ('employee_id', 'department', 'designation', 'joining_date')
        }),
        ('Qualifications', {
            'fields': ('qualification', 'specialization', 'experience_years')
        }),
        ('Statistics', {
            'fields': ('total_courses', 'total_students'),
            'classes': ('collapse',)
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(TeacherQualification)
class TeacherQualificationAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'title', 'institution', 'completion_year')
    list_filter = ('completion_year',)
    search_fields = ('teacher__user__email', 'title', 'institution')
