from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages


def home(request):
    """Home/landing page"""
    if request.user.is_authenticated:
        # Redirect to appropriate dashboard based on user type
        if request.user.user_type == 'ORGANIZATION':
            return redirect('organization-dashboard')
        elif request.user.user_type == 'TEACHER':
            return redirect('teacher-dashboard')
        elif request.user.user_type == 'STUDENT':
            return redirect('student-dashboard')
        elif request.user.user_type == 'SUPPORT':
            return redirect('support-dashboard')
        elif request.user.is_superuser:
            return redirect('admin:index')
    
    return render(request, 'dashboard/home.html')


@login_required(login_url='login')
def user_dashboard(request):
    """Generic user dashboard (redirects to specific dashboard)"""
    if request.user.user_type == 'ORGANIZATION':
        return redirect('organization-dashboard')
    elif request.user.user_type == 'TEACHER':
        return redirect('teacher-dashboard')
    elif request.user.user_type == 'STUDENT':
        return redirect('student-dashboard')
    elif request.user.user_type == 'SUPPORT':
        return redirect('support-dashboard')
    elif request.user.is_superuser:
        return redirect('admin:index')
    else:
        return render(request, 'dashboard/user_dashboard.html', {'user': request.user})


@login_required(login_url='login')
def settings(request):
    """User settings"""
    if request.method == 'POST':
        # Handle settings update
        pass
    
    context = {
        'user': request.user,
    }
    return render(request, 'dashboard/settings.html', context)
