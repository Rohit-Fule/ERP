from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .models import CustomUser


def _create_user_and_redirect(email, first_name, last_name, password, user_type, phone=''):
    """Helper function to create user and redirect based on type"""
    if CustomUser.objects.filter(email=email).exists():
        return None, 'Email already registered!'
    
    user = CustomUser.objects.create_user(
        email=email,
        first_name=first_name,
        last_name=last_name,
        password=password,
        user_type=user_type,
        phone=phone
    )
    return user, None


def _redirect_by_user_type(user):
    """Redirect based on user type"""
    if user.user_type == 'ORGANIZATION':
        return redirect('organization-dashboard')
    elif user.user_type == 'TEACHER':
        return redirect('teacher-dashboard')
    elif user.user_type == 'STUDENT':
        return redirect('student-dashboard')
    elif user.user_type == 'SUPPORT':
        return redirect('support-dashboard')
    elif user.user_type == 'ADMIN':
        return redirect('admin:index')
    else:
        return redirect('home')


# ============ GENERIC LOGIN/REGISTER ============

def register(request):
    """User registration view"""
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user_type = request.POST.get('user_type', 'STUDENT')
        phone = request.POST.get('phone', '')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return render(request, 'users/register.html')

        user, error = _create_user_and_redirect(email, first_name, last_name, password, user_type, phone)
        if error:
            messages.error(request, error)
            return render(request, 'users/register.html')
        
        messages.success(request, 'Registration successful! Please log in.')
        return redirect('login')

    context = {
        'user_types': CustomUser.USER_TYPE_CHOICES
    }
    return render(request, 'users/register.html', context)


@require_http_methods(["GET", "POST"])
def user_login(request):
    """User login view"""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return _redirect_by_user_type(user)
        else:
            messages.error(request, 'Invalid email or password!')

    return render(request, 'users/login.html')


# ============ STUDENT LOGIN/REGISTER ============

@require_http_methods(["GET", "POST"])
def student_login(request):
    """Student login view"""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None and user.user_type == 'STUDENT':
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name}!')
            return redirect('student-dashboard')
        else:
            messages.error(request, 'Invalid email or password for student account!')

    return render(request, 'users/student_login.html')


def student_register(request):
    """Student registration view"""
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone = request.POST.get('phone', '')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return render(request, 'users/student_register.html')

        user, error = _create_user_and_redirect(email, first_name, last_name, password, 'STUDENT', phone)
        if error:
            messages.error(request, error)
            return render(request, 'users/student_register.html')
        
        messages.success(request, 'Registration successful! Please log in.')
        return redirect('student-login')

    return render(request, 'users/student_register.html')


# ============ TEACHER LOGIN/REGISTER ============

@require_http_methods(["GET", "POST"])
def teacher_login(request):
    """Teacher login view"""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None and user.user_type == 'TEACHER':
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name}!')
            return redirect('teacher-dashboard')
        else:
            messages.error(request, 'Invalid email or password for teacher account!')

    return render(request, 'users/teacher_login.html')


def teacher_register(request):
    """Teacher registration view"""
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone = request.POST.get('phone', '')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return render(request, 'users/teacher_register.html')

        user, error = _create_user_and_redirect(email, first_name, last_name, password, 'TEACHER', phone)
        if error:
            messages.error(request, error)
            return render(request, 'users/teacher_register.html')
        
        messages.success(request, 'Registration successful! Please log in.')
        return redirect('teacher-login')

    return render(request, 'users/teacher_register.html')


# ============ ORGANIZATION LOGIN/REGISTER ============

@require_http_methods(["GET", "POST"])
def organization_login(request):
    """Organization login view"""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None and user.user_type == 'ORGANIZATION':
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name}!')
            return redirect('organization-dashboard')
        else:
            messages.error(request, 'Invalid email or password for organization account!')

    return render(request, 'users/organization_login.html')


def organization_register(request):
    """Organization registration view"""
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone = request.POST.get('phone', '')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return render(request, 'users/organization_register.html')

        user, error = _create_user_and_redirect(email, first_name, last_name, password, 'ORGANIZATION', phone)
        if error:
            messages.error(request, error)
            return render(request, 'users/organization_register.html')
        
        messages.success(request, 'Registration successful! Please log in.')
        return redirect('organization-login')

    return render(request, 'users/organization_register.html')


# ============ SUPPORT LOGIN/REGISTER ============

@require_http_methods(["GET", "POST"])
def support_login(request):
    """Support team login view"""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None and user.user_type == 'SUPPORT':
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name}!')
            return redirect('support-dashboard')
        else:
            messages.error(request, 'Invalid email or password for support account!')

    return render(request, 'users/support_login.html')


def support_register(request):
    """Support team registration view"""
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone = request.POST.get('phone', '')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return render(request, 'users/support_register.html')

        user, error = _create_user_and_redirect(email, first_name, last_name, password, 'SUPPORT', phone)
        if error:
            messages.error(request, error)
            return render(request, 'users/support_register.html')
        
        messages.success(request, 'Registration successful! Please log in.')
        return redirect('support-login')

    return render(request, 'users/support_register.html')


@login_required(login_url='login')
def user_logout(request):
    """User logout view"""
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')


@login_required(login_url='login')
def profile(request):
    """User profile view"""
    user = request.user
    
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.phone = request.POST.get('phone', user.phone)
        user.bio = request.POST.get('bio', user.bio)
        user.address = request.POST.get('address', user.address)
        user.city = request.POST.get('city', user.city)
        user.state = request.POST.get('state', user.state)
        user.postal_code = request.POST.get('postal_code', user.postal_code)
        user.country = request.POST.get('country', user.country)
        
        if 'profile_image' in request.FILES:
            user.profile_image = request.FILES['profile_image']
        
        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')
    
    context = {
        'user': user
    }
    return render(request, 'users/profile.html', context)
