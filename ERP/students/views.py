from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from courses.models import Enrollment, Assignment, Submission
from .models import Student
from .forms import StudentProfileForm


@login_required(login_url='login')
def student_dashboard(request):
    """Student dashboard view"""
    if request.user.user_type != 'STUDENT':
        messages.error(request, 'Only students can access this page.')
        return redirect('home')
    
    try:
        student = request.user.student_profile
    except Student.DoesNotExist:
        messages.error(request, 'Student profile not found. Please complete your profile.')
        return redirect('profile')
    
    # Get student's enrollments
    enrollments = Enrollment.objects.filter(student=request.user)
    
    # Get pending assignments
    pending_assignments = Assignment.objects.filter(
        course__enrollments__student=request.user,
        course__enrollments__status='ACTIVE'
    ).order_by('due_date')
    
    context = {
        'student': student,
        'enrollments': enrollments,
        'pending_assignments': pending_assignments,
        'total_enrolled_courses': enrollments.filter(status='ACTIVE').count(),
    }
    return render(request, 'students/dashboard.html', context)


@login_required(login_url='login')
def student_courses(request):
    """View student's enrolled courses"""
    if request.user.user_type != 'STUDENT':
        messages.error(request, 'Only students can access this page.')
        return redirect('home')
    
    enrollments = Enrollment.objects.filter(student=request.user, status='ACTIVE')
    
    context = {
        'enrollments': enrollments,
    }
    return render(request, 'students/courses.html', context)


@login_required(login_url='login')
def student_assignments(request):
    """View student's assignments"""
    if request.user.user_type != 'STUDENT':
        messages.error(request, 'Only students can access this page.')
        return redirect('home')
    
    # Get assignments from enrolled courses
    assignments = Assignment.objects.filter(
        course__enrollments__student=request.user,
        course__enrollments__status='ACTIVE'
    ).order_by('due_date')
    
    # Get submissions for these assignments
    submissions = Submission.objects.filter(student=request.user)
    submission_dict = {sub.assignment_id: sub for sub in submissions}
    
    context = {
        'assignments': assignments,
        'submission_dict': submission_dict,
    }
    return render(request, 'students/assignments.html', context)


@login_required(login_url='login')
def assignment_detail(request, assignment_id):
    """View assignment details and submission"""
    if request.user.user_type != 'STUDENT':
        messages.error(request, 'Only students can access this page.')
        return redirect('home')
    
    try:
        assignment = Assignment.objects.get(id=assignment_id)
        # Check if student is enrolled in the course
        enrollment = Enrollment.objects.get(
            student=request.user,
            course=assignment.course,
            status='ACTIVE'
        )
    except (Assignment.DoesNotExist, Enrollment.DoesNotExist):
        messages.error(request, 'Assignment not found or you do not have access.')
        return redirect('student-assignments')
    
    # Get submission if exists
    submission = Submission.objects.filter(
        assignment=assignment,
        student=request.user
    ).first()
    
    context = {
        'assignment': assignment,
        'submission': submission,
    }
    return render(request, 'students/assignment_detail.html', context)


@login_required(login_url='login')
def student_profile(request):
    """Student profile view"""
    if request.user.user_type != 'STUDENT':
        messages.error(request, 'Only students can access this page.')
        return redirect('home')
    
    try:
        student = request.user.student_profile
    except Student.DoesNotExist:
        messages.error(request, 'Student profile not found.')
        return redirect('profile')
    
    context = {
        'student': student,
    }
    return render(request, 'students/profile.html', context)


@login_required(login_url='login')
def student_profile_edit(request):
    """Create or edit student profile"""
    if request.user.user_type != 'STUDENT':
        messages.error(request, 'Only student users can access this page.')
        return redirect('home')
    
    try:
        student = request.user.student_profile
        is_new = False
    except Student.DoesNotExist:
        student = Student(user=request.user)
        is_new = True
    
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, instance=student)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            
            if is_new:
                messages.success(request, 'Student profile created successfully!')
                return redirect('student-dashboard')
            else:
                messages.success(request, 'Student profile updated successfully!')
                return redirect('student-profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentProfileForm(instance=student)
    
    context = {
        'form': form,
        'is_new': is_new,
        'title': 'Create Student Profile' if is_new else 'Edit Student Profile'
    }
    return render(request, 'students/profile_edit.html', context)
