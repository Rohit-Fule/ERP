from django.db import models
from django.utils import timezone
from users.models import CustomUser
from organizations.models import Organization


class Course(models.Model):
    """Course model"""
    
    STATUS_CHOICES = (
        ('DRAFT', 'Draft'),
        ('ACTIVE', 'Active'),
        ('ARCHIVED', 'Archived'),
    )
    
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='courses')
    instructor = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='courses_taught')
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    code = models.CharField(max_length=50, unique=True)
    
    category = models.CharField(max_length=100, blank=True)
    credits = models.IntegerField(default=3)
    capacity = models.IntegerField(default=50)
    
    thumbnail = models.ImageField(upload_to='course_thumbnails/', blank=True, null=True)
    
    start_date = models.DateField()
    end_date = models.DateField()
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DRAFT')
    
    # Enrollment tracking
    current_enrollment = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['-created_at']
        unique_together = ('organization', 'code')

    def __str__(self):
        return f'{self.code} - {self.title}'


class Enrollment(models.Model):
    """Student enrollment in courses"""
    
    STATUS_CHOICES = (
        ('ACTIVE', 'Active'),
        ('COMPLETED', 'Completed'),
        ('DROPPED', 'Dropped'),
    )
    
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    
    enrollment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    
    grade = models.CharField(max_length=5, blank=True, null=True)
    attendance_percentage = models.FloatField(default=0)
    marks_obtained = models.FloatField(blank=True, null=True)
    
    completed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Enrollment'
        verbose_name_plural = 'Enrollments'
        unique_together = ('student', 'course')
        ordering = ['-enrollment_date']

    def __str__(self):
        return f'{self.student.email} - {self.course.code}'


class Assignment(models.Model):
    """Course assignments"""
    
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    due_date = models.DateTimeField()
    total_marks = models.FloatField(default=100)
    
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Assignment'
        verbose_name_plural = 'Assignments'
        ordering = ['-due_date']

    def __str__(self):
        return f'{self.course.code} - {self.title}'


class Submission(models.Model):
    """Student submissions for assignments"""
    
    STATUS_CHOICES = (
        ('SUBMITTED', 'Submitted'),
        ('GRADED', 'Graded'),
        ('LATE', 'Late Submission'),
    )
    
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='submissions')
    
    file = models.FileField(upload_to='submissions/')
    submission_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='SUBMITTED')
    
    marks_obtained = models.FloatField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    graded_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='graded_submissions')
    graded_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Submission'
        verbose_name_plural = 'Submissions'
        unique_together = ('assignment', 'student')
        ordering = ['-submission_date']

    def __str__(self):
        return f'{self.student.email} - {self.assignment.title}'
