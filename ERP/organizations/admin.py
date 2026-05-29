from django.contrib import admin
from .models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('organization_name', 'contact_email', 'is_verified', 'is_active', 'total_students', 'total_teachers', 'created_at')
    list_filter = ('is_verified', 'is_active', 'created_at')
    search_fields = ('organization_name', 'contact_email', 'registration_number')
    readonly_fields = ('created_at', 'updated_at', 'total_students', 'total_teachers', 'total_courses')
    
    fieldsets = (
        ('Organization Details', {
            'fields': ('user', 'organization_name', 'registration_number', 'website', 'establishment_year')
        }),
        ('Logo & Banner', {
            'fields': ('logo', 'banner')
        }),
        ('Contact Information', {
            'fields': ('contact_email', 'contact_phone')
        }),
        ('Headquarters Address', {
            'fields': ('headquarters_address', 'headquarters_city', 'headquarters_state', 'headquarters_postal_code', 'headquarters_country')
        }),
        ('Statistics', {
            'fields': ('total_students', 'total_teachers', 'total_courses'),
            'classes': ('collapse',)
        }),
        ('Status', {
            'fields': ('is_verified', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
