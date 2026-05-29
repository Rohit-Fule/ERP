from django.db import models
from users.models import CustomUser
from organizations.models import Organization


class Student(models.Model):
    """Student profile model"""
    
    ACADEMIC_STATUS_CHOICES = (
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
        ('GRADUATED', 'Graduated'),
        ('SUSPENDED', 'Suspended'),
    )
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student_profile')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='students')
    
    # Enrollment Details
    enrollment_number = models.CharField(max_length=100, unique=True)
    roll_number = models.CharField(max_length=100, blank=True, null=True)
    
    # Academic Information
    program = models.CharField(max_length=255)
    current_year = models.IntegerField(default=1, help_text="Current year of study")
    semester = models.IntegerField(default=1)
    batch_year = models.IntegerField()
    admission_date = models.DateField(help_text="Date of admission")
    
    academic_status = models.CharField(max_length=20, choices=ACADEMIC_STATUS_CHOICES, default='ACTIVE')
    
    # Personal Information
    date_of_birth = models.DateField(blank=True, null=True)
    parent_name = models.CharField(max_length=255, blank=True, null=True)
    parent_phone = models.CharField(max_length=20, blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=255, blank=True, null=True)
    emergency_contact_phone = models.CharField(max_length=20, blank=True, null=True)
    
    # Document Uploads
    admission_letter = models.FileField(upload_to='student_documents/admission_letters/', blank=True, null=True)
    identity_proof = models.FileField(upload_to='student_documents/identity_proofs/', blank=True, null=True)
    certificate_10th = models.FileField(upload_to='student_documents/certificates/', blank=True, null=True)
    certificate_12th = models.FileField(upload_to='student_documents/certificates/', blank=True, null=True)
    medical_certificate = models.FileField(upload_to='student_documents/medical/', blank=True, null=True)
    
    # Academic Stats
    total_courses_enrolled = models.IntegerField(default=0)
    total_courses_completed = models.IntegerField(default=0)
    current_gpa = models.FloatField(default=0.0)
    
    # Dates
    enrollment_date = models.DateField()
    expected_graduation_date = models.DateField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.get_full_name()} ({self.enrollment_number})'
