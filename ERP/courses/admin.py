from django.contrib import admin
from .models import Course, Enrollment, Assignment, Submission


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'organization', 'instructor', 'status', 'current_enrollment', 'capacity', 'created_at')
    list_filter = ('status', 'organization', 'created_at')
    search_fields = ('title', 'code', 'description')
    readonly_fields = ('created_at', 'updated_at', 'current_enrollment')
    
    fieldsets = (
        ('Course Information', {
            'fields': ('organization', 'title', 'code', 'description', 'category')
        }),
        ('Instructor & Capacity', {
            'fields': ('instructor', 'capacity', 'current_enrollment', 'credits')
        }),
        ('Course Dates', {
            'fields': ('start_date', 'end_date')
        }),
        ('Media', {
            'fields': ('thumbnail',)
        }),
        ('Status', {
            'fields': ('status',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'status', 'grade', 'attendance_percentage', 'enrollment_date')
    list_filter = ('status', 'course', 'enrollment_date')
    search_fields = ('student__email', 'course__code')
    readonly_fields = ('enrollment_date',)


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'due_date', 'total_marks', 'created_by')
    list_filter = ('course', 'due_date', 'created_at')
    search_fields = ('title', 'course__code')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('student', 'assignment', 'status', 'marks_obtained', 'submission_date')
    list_filter = ('status', 'assignment', 'submission_date')
    search_fields = ('student__email', 'assignment__title')
    readonly_fields = ('submission_date', 'graded_at')
