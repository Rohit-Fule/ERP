from django.db import models
from users.models import CustomUser


class Organization(models.Model):
    """Organization/Institution model"""
    
    ACCREDITATION_CHOICES = (
        ('NAAC', 'NAAC'),
        ('ACCBIND', 'ACCBIND'),
        ('NBA', 'NBA'),
        ('OTHER', 'Other'),
        ('NONE', 'None'),
    )
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='organization_profile')
    organization_name = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=100, unique=True)
    website = models.URLField(blank=True, null=True)
    establishment_year = models.IntegerField(blank=True, null=True)
    
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='organization_logos/', blank=True, null=True)
    banner = models.ImageField(upload_to='organization_banners/', blank=True, null=True)
    
    # Contact Information
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    principal_name = models.CharField(max_length=255, blank=True, null=True)
    principal_email = models.EmailField(blank=True, null=True)
    principal_phone = models.CharField(max_length=20, blank=True, null=True)
    
    # Address
    headquarters_address = models.CharField(max_length=255)
    headquarters_city = models.CharField(max_length=100)
    headquarters_state = models.CharField(max_length=100)
    headquarters_postal_code = models.CharField(max_length=20)
    headquarters_country = models.CharField(max_length=100)
    
    # Organization Details
    accreditation_type = models.CharField(max_length=50, choices=ACCREDITATION_CHOICES, default='NONE')
    accreditation_number = models.CharField(max_length=100, blank=True, null=True)
    university_affiliation = models.CharField(max_length=255, blank=True, null=True)
    gstin = models.CharField(max_length=20, blank=True, null=True, verbose_name="GSTIN")
    
    # Documents
    registration_certificate = models.FileField(upload_to='organization_documents/registration/', blank=True, null=True)
    accreditation_certificate = models.FileField(upload_to='organization_documents/accreditation/', blank=True, null=True)
    license = models.FileField(upload_to='organization_documents/licenses/', blank=True, null=True)
    
    # Stats
    total_students = models.IntegerField(default=0)
    total_teachers = models.IntegerField(default=0)
    total_courses = models.IntegerField(default=0)
    
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'
        ordering = ['-created_at']

    def __str__(self):
        return self.organization_name
