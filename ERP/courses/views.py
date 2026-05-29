from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .models import Course, Enrollment, Assignment, Submission


@login_required(login_url='login')
def course_list(request):
    """List all available courses"""
    courses = Course.objects.filter(status='ACTIVE')
    
    context = {
        'courses': courses,
    }
    return render(request, 'courses/course_list.html', context)


@login_required(login_url='login')
def course_detail(request, course_id):
    """View course details"""
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        messages.error(request, 'Course not found.')
        return redirect('course-list')
    
    # Check if student is enrolled
    is_enrolled = Enrollment.objects.filter(
        student=request.user,
        course=course
    ).exists()
    
    context = {
        'course': course,
        'is_enrolled': is_enrolled,
    }
    return render(request, 'courses/course_detail.html', context)


@login_required(login_url='login')
@require_http_methods(["POST"])
def enroll_course(request, course_id):
    """Enroll student in a course"""
    if request.user.user_type != 'STUDENT':
        messages.error(request, 'Only students can enroll in courses.')
        return redirect('course-list')
    
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        messages.error(request, 'Course not found.')
        return redirect('course-list')
    
    if course.current_enrollment >= course.capacity:
        messages.error(request, 'Course is full.')
        return redirect('course-detail', course_id=course_id)
    
    enrollment, created = Enrollment.objects.get_or_create(
        student=request.user,
        course=course
    )
    
    if created:
        course.current_enrollment += 1
        course.save()
        messages.success(request, f'Successfully enrolled in {course.title}!')
    else:
        messages.info(request, 'You are already enrolled in this course.')
    
    return redirect('course-detail', course_id=course_id)
