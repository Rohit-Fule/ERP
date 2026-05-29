from django.db import models
from users.models import CustomUser
from organizations.models import Organization


class Teacher(models.Model):
    """Teacher profile model"""
    
    QUALIFICATION_CHOICES = (
        ('BACHELOR', "Bachelor's Degree"),
        ('MASTER', "Master's Degree"),
        ('PHD', 'PhD'),
        ('POSTDOC', 'Post-Doctorate'),
        ('OTHER', 'Other'),
    )
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='teacher_profile')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='teachers')
    
    # Employment Details
    employee_id = models.CharField(max_length=100, unique=True)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    joining_date = models.DateField()
    
    # Qualifications
    qualification = models.CharField(max_length=50, choices=QUALIFICATION_CHOICES)
    specialization = models.CharField(max_length=255, blank=True, null=True)
    experience_years = models.IntegerField(default=0)
    
    # Personal Details
    date_of_birth = models.DateField(blank=True, null=True)
    bank_account_number = models.CharField(max_length=50, blank=True, null=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    pan_number = models.CharField(max_length=20, blank=True, null=True)
    
    # Document Uploads
    degree_certificate = models.FileField(upload_to='teacher_documents/degrees/', blank=True, null=True)
    identity_proof = models.FileField(upload_to='teacher_documents/identity/', blank=True, null=True)
    teaching_license = models.FileField(upload_to='teacher_documents/licenses/', blank=True, null=True)
    experience_certificate = models.FileField(upload_to='teacher_documents/experience/', blank=True, null=True)
    research_publications = models.FileField(upload_to='teacher_documents/research/', blank=True, null=True)
    
    # Performance & Recognition
    performance_rating = models.FloatField(default=0.0, help_text="Average performance rating")
    total_courses = models.IntegerField(default=0)
    total_students = models.IntegerField(default=0)
    
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.get_full_name()} ({self.employee_id})'


class TeacherQualification(models.Model):
    """Teacher qualifications/certifications"""
    
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='qualifications')
    title = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    completion_year = models.IntegerField()
    certificate = models.FileField(upload_to='teacher_certificates/', blank=True, null=True)

    class Meta:
        verbose_name = 'Teacher Qualification'
        verbose_name_plural = 'Teacher Qualifications'

    def __str__(self):
        return f'{self.teacher.user.email} - {self.title}'
