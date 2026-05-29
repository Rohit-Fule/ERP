from django.db import models
from users.models import CustomUser


class Ticket(models.Model):
    """Support ticket model"""
    
    PRIORITY_CHOICES = (
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('CRITICAL', 'Critical'),
    )
    
    STATUS_CHOICES = (
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
        ('CLOSED', 'Closed'),
        ('REOPENED', 'Reopened'),
    )
    
    CATEGORY_CHOICES = (
        ('TECHNICAL', 'Technical Issue'),
        ('ACCOUNT', 'Account Issue'),
        ('COURSE', 'Course Related'),
        ('ENROLLMENT', 'Enrollment'),
        ('PAYMENT', 'Payment'),
        ('OTHER', 'Other'),
    )
    
    ticket_id = models.CharField(max_length=50, unique=True, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='support_tickets')
    
    subject = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='MEDIUM')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')
    
    attachment = models.FileField(upload_to='ticket_attachments/', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(blank=True, null=True)
    
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tickets')

    class Meta:
        verbose_name = 'Support Ticket'
        verbose_name_plural = 'Support Tickets'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.ticket_id:
            import uuid
            self.ticket_id = f'TKT-{uuid.uuid4().hex[:8].upper()}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.ticket_id} - {self.subject}'


class TicketResponse(models.Model):
    """Support ticket responses/comments"""
    
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='responses')
    responder = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='ticket_responses')
    
    message = models.TextField()
    attachment = models.FileField(upload_to='ticket_responses/', blank=True, null=True)
    
    is_internal = models.BooleanField(default=False)  # Internal notes only visible to support team
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Ticket Response'
        verbose_name_plural = 'Ticket Responses'
        ordering = ['-created_at']

    def __str__(self):
        return f'Response to {self.ticket.ticket_id}'


class SupportTeamMember(models.Model):
    """Support team member profile"""
    
    ROLE_CHOICES = (
        ('AGENT', 'Support Agent'),
        ('SUPERVISOR', 'Supervisor'),
        ('MANAGER', 'Manager'),
        ('ADMIN', 'Support Admin'),
    )
    
    SHIFT_CHOICES = (
        ('MORNING', 'Morning (6 AM - 2 PM)'),
        ('AFTERNOON', 'Afternoon (2 PM - 10 PM)'),
        ('NIGHT', 'Night (10 PM - 6 AM)'),
        ('FLEXIBLE', 'Flexible'),
    )
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='support_profile')
    
    # Employment Details
    employee_id = models.CharField(max_length=100, unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    department = models.CharField(max_length=100)
    joining_date = models.DateField()
    
    # Skill & Specialization
    specialization = models.CharField(max_length=255, blank=True, null=True)
    assigned_categories = models.CharField(max_length=255, blank=True, null=True, help_text="Comma-separated categories")
    
    # Shift & Availability
    shift = models.CharField(max_length=20, choices=SHIFT_CHOICES, default='FLEXIBLE')
    languages_spoken = models.CharField(max_length=255, blank=True, null=True, help_text="Comma-separated languages")
    
    # Personal Details
    date_of_birth = models.DateField(blank=True, null=True)
    bank_account_number = models.CharField(max_length=50, blank=True, null=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    
    # Documents
    identity_proof = models.FileField(upload_to='support_documents/identity/', blank=True, null=True)
    degree_certificate = models.FileField(upload_to='support_documents/degrees/', blank=True, null=True)
    certifications = models.FileField(upload_to='support_documents/certifications/', blank=True, null=True)
    
    # Performance Metrics
    total_tickets_handled = models.IntegerField(default=0)
    total_tickets_resolved = models.IntegerField(default=0)
    average_rating = models.FloatField(default=0.0)
    average_resolution_time = models.IntegerField(default=0, help_text="In hours")
    
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Support Team Member'
        verbose_name_plural = 'Support Team Members'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.get_full_name()} ({self.employee_id})'


class TicketRating(models.Model):
    """Rating for resolved support tickets"""
    
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE, related_name='rating')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    feedback = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Ticket Rating'
        verbose_name_plural = 'Ticket Ratings'

    def __str__(self):
        return f'{self.ticket.ticket_id} - {self.rating} stars'
