from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .models import Organization
from .forms import OrganizationProfileForm


@login_required(login_url='login')
def organization_dashboard(request):
    """Organization dashboard view"""
    try:
        org = request.user.organization_profile
    except Organization.DoesNotExist:
        messages.error(request, 'Organization profile not found. Please complete your profile.')
        return redirect('profile')
    
    context = {
        'organization': org,
        'total_students': org.total_students,
        'total_teachers': org.total_teachers,
        'total_courses': org.total_courses,
    }
    return render(request, 'organizations/dashboard.html', context)


@login_required(login_url='login')
@require_http_methods(["GET", "POST"])
def organization_settings(request):
    """Organization settings view"""
    try:
        org = request.user.organization_profile
    except Organization.DoesNotExist:
        messages.error(request, 'Organization profile not found.')
        return redirect('profile')
    
    if request.method == 'POST':
        org.organization_name = request.POST.get('organization_name', org.organization_name)
        org.contact_email = request.POST.get('contact_email', org.contact_email)
        org.contact_phone = request.POST.get('contact_phone', org.contact_phone)
        org.website = request.POST.get('website', org.website)
        org.description = request.POST.get('description', org.description)
        
        # Address fields
        org.headquarters_address = request.POST.get('address', org.headquarters_address)
        org.headquarters_city = request.POST.get('city', org.headquarters_city)
        org.headquarters_state = request.POST.get('state', org.headquarters_state)
        org.headquarters_postal_code = request.POST.get('postal_code', org.headquarters_postal_code)
        org.headquarters_country = request.POST.get('country', org.headquarters_country)
        
        # Handle file uploads
        if 'logo' in request.FILES:
            org.logo = request.FILES['logo']
        if 'banner' in request.FILES:
            org.banner = request.FILES['banner']
        
        org.save()
        messages.success(request, 'Organization settings updated successfully!')
        return redirect('organization-dashboard')
    
    context = {
        'organization': org
    }
    return render(request, 'organizations/settings.html', context)


@login_required(login_url='login')
def organization_members(request):
    """View organization members (teachers and students)"""
    try:
        org = request.user.organization_profile
    except Organization.DoesNotExist:
        messages.error(request, 'Organization profile not found.')
        return redirect('profile')
    
    context = {
        'organization': org,
    }
    return render(request, 'organizations/members.html', context)


@login_required(login_url='login')
@require_http_methods(["GET", "POST"])
def organization_profile(request):
    """Create or edit organization profile"""
    if request.user.user_type != 'ORGANIZATION':
        messages.error(request, 'Only organization users can access this page.')
        return redirect('home')
    
    try:
        org = request.user.organization_profile
        is_new = False
    except Organization.DoesNotExist:
        org = Organization(user=request.user)
        is_new = True
    
    if request.method == 'POST':
        form = OrganizationProfileForm(request.POST, request.FILES, instance=org)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            
            if is_new:
                messages.success(request, 'Organization profile created successfully!')
                return redirect('organization-dashboard')
            else:
                messages.success(request, 'Organization profile updated successfully!')
                return redirect('organization-profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = OrganizationProfileForm(instance=org)
    
    context = {
        'form': form,
        'is_new': is_new,
        'title': 'Create Organization Profile' if is_new else 'Edit Organization Profile'
    }
    return render(request, 'organizations/profile.html', context)
