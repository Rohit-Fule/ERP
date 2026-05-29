from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from courses.models import Course, Enrollment, Assignment
from .models import Teacher
from .forms import TeacherProfileForm


@login_required(login_url='login')
def teacher_dashboard(request):
    """Teacher dashboard view"""
    if request.user.user_type != 'TEACHER':
        messages.error(request, 'Only teachers can access this page.')
        return redirect('home')
    
    try:
        teacher = request.user.teacher_profile
    except Teacher.DoesNotExist:
        messages.error(request, 'Teacher profile not found. Please complete your profile.')
        return redirect('profile')
    
    # Get teacher's courses
    courses = Course.objects.filter(instructor=request.user)
    total_students = Enrollment.objects.filter(course__instructor=request.user).count()
    
    context = {
        'teacher': teacher,
        'courses': courses,
        'total_courses': courses.count(),
        'total_students': total_students,
    }
    return render(request, 'teachers/dashboard.html', context)


@login_required(login_url='login')
def teacher_courses(request):
    """View teacher's courses"""
    if request.user.user_type != 'TEACHER':
        messages.error(request, 'Only teachers can access this page.')
        return redirect('home')
    
    courses = Course.objects.filter(instructor=request.user)
    
    context = {
        'courses': courses,
    }
    return render(request, 'teachers/courses.html', context)


@login_required(login_url='login')
def course_students(request, course_id):
    """View students enrolled in a course"""
    if request.user.user_type != 'TEACHER':
        messages.error(request, 'Only teachers can access this page.')
        return redirect('home')
    
    try:
        course = Course.objects.get(id=course_id, instructor=request.user)
    except Course.DoesNotExist:
        messages.error(request, 'Course not found or you do not have access.')
        return redirect('teacher-courses')
    
    enrollments = Enrollment.objects.filter(course=course)
    
    context = {
        'course': course,
        'enrollments': enrollments,
    }
    return render(request, 'teachers/course_students.html', context)


@login_required(login_url='login')
@require_http_methods(["GET", "POST"])
def create_assignment(request, course_id):
    """Create assignment for a course"""
    if request.user.user_type != 'TEACHER':
        messages.error(request, 'Only teachers can create assignments.')
        return redirect('home')
    
    try:
        course = Course.objects.get(id=course_id, instructor=request.user)
    except Course.DoesNotExist:
        messages.error(request, 'Course not found or you do not have access.')
        return redirect('teacher-courses')
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        total_marks = request.POST.get('total_marks', 100)
        
        assignment = Assignment.objects.create(
            course=course,
            title=title,
            description=description,
            due_date=due_date,
            total_marks=total_marks,
            created_by=request.user
        )
        
        messages.success(request, 'Assignment created successfully!')
        return redirect('course-students', course_id=course_id)
    
    context = {
        'course': course,
    }
    return render(request, 'teachers/create_assignment.html', context)


@login_required(login_url='login')
def teacher_profile(request):
    """Teacher profile view"""
    if request.user.user_type != 'TEACHER':
        messages.error(request, 'Only teachers can access this page.')
        return redirect('home')
    
    try:
        teacher = request.user.teacher_profile
    except Teacher.DoesNotExist:
        messages.error(request, 'Teacher profile not found.')
        return redirect('profile')
    
    context = {
        'teacher': teacher,
    }
    return render(request, 'teachers/profile.html', context)


@login_required(login_url='login')
@require_http_methods(["GET", "POST"])
def teacher_profile_edit(request):
    """Create or edit teacher profile"""
    if request.user.user_type != 'TEACHER':
        messages.error(request, 'Only teacher users can access this page.')
        return redirect('home')
    
    try:
        teacher = request.user.teacher_profile
        is_new = False
    except Teacher.DoesNotExist:
        teacher = Teacher(user=request.user)
        is_new = True
    
    if request.method == 'POST':
        form = TeacherProfileForm(request.POST, instance=teacher)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            
            if is_new:
                messages.success(request, 'Teacher profile created successfully!')
                return redirect('teacher-dashboard')
            else:
                messages.success(request, 'Teacher profile updated successfully!')
                return redirect('teacher-profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = TeacherProfileForm(instance=teacher)
    
    context = {
        'form': form,
        'is_new': is_new,
        'title': 'Create Teacher Profile' if is_new else 'Edit Teacher Profile'
    }
    return render(request, 'teachers/profile_edit.html', context)
