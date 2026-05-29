from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.utils import timezone
from .models import Ticket, TicketResponse, SupportTeamMember, TicketRating
from .forms import SupportProfileForm


@login_required(login_url='login')
def support_dashboard(request):
    """Support team dashboard"""
    if request.user.user_type != 'SUPPORT':
        messages.error(request, 'Only support team members can access this page.')
        return redirect('home')
    
    try:
        support_member = request.user.support_profile
    except SupportTeamMember.DoesNotExist:
        messages.error(request, 'Support profile not found.')
        return redirect('profile')
    
    # Get tickets statistics
    open_tickets = Ticket.objects.filter(status='OPEN').count()
    in_progress_tickets = Ticket.objects.filter(status='IN_PROGRESS').count()
    resolved_tickets = Ticket.objects.filter(status='RESOLVED').count()
    
    # Get assigned tickets for this support member
    assigned_tickets = Ticket.objects.filter(assigned_to=request.user)
    
    # Get high priority tickets
    high_priority = Ticket.objects.filter(priority__in=['HIGH', 'CRITICAL']).count()
    
    context = {
        'support_member': support_member,
        'open_tickets': open_tickets,
        'in_progress_tickets': in_progress_tickets,
        'resolved_tickets': resolved_tickets,
        'assigned_tickets': assigned_tickets,
        'high_priority': high_priority,
    }
    return render(request, 'support/dashboard.html', context)


@login_required(login_url='login')
def ticket_list(request):
    """List all support tickets"""
    if request.user.user_type != 'SUPPORT':
        messages.error(request, 'Only support team members can access this page.')
        return redirect('home')
    
    # Filter tickets
    status_filter = request.GET.get('status', '')
    priority_filter = request.GET.get('priority', '')
    
    tickets = Ticket.objects.all()
    
    if status_filter:
        tickets = tickets.filter(status=status_filter)
    if priority_filter:
        tickets = tickets.filter(priority=priority_filter)
    
    context = {
        'tickets': tickets,
        'status_filter': status_filter,
        'priority_filter': priority_filter,
        'status_choices': Ticket.STATUS_CHOICES,
        'priority_choices': Ticket.PRIORITY_CHOICES,
    }
    return render(request, 'support/ticket_list.html', context)


@login_required(login_url='login')
def ticket_detail(request, ticket_id):
    """View ticket details and manage it"""
    if request.user.user_type != 'SUPPORT':
        messages.error(request, 'Only support team members can access this page.')
        return redirect('home')
    
    try:
        ticket = Ticket.objects.get(ticket_id=ticket_id)
    except Ticket.DoesNotExist:
        messages.error(request, 'Ticket not found.')
        return redirect('support-ticket-list')
    
    if request.method == 'POST':
        # Update ticket status or assignment
        if 'status' in request.POST:
            ticket.status = request.POST.get('status')
            if ticket.status == 'RESOLVED':
                ticket.resolved_at = timezone.now()
            ticket.save()
            messages.success(request, 'Ticket status updated!')
        
        if 'assigned_to' in request.POST:
            assigned_user_id = request.POST.get('assigned_to')
            if assigned_user_id:
                ticket.assigned_to_id = assigned_user_id
                ticket.save()
                messages.success(request, 'Ticket assigned!')
        
        # Add response
        if 'message' in request.POST:
            message = request.POST.get('message')
            is_internal = 'is_internal' in request.POST
            
            TicketResponse.objects.create(
                ticket=ticket,
                responder=request.user,
                message=message,
                is_internal=is_internal
            )
            messages.success(request, 'Response added!')
            return redirect('support-ticket-detail', ticket_id=ticket_id)
    
    responses = ticket.responses.all()
    support_team = SupportTeamMember.objects.filter(is_active=True)
    
    context = {
        'ticket': ticket,
        'responses': responses,
        'support_team': support_team,
        'status_choices': Ticket.STATUS_CHOICES,
    }
    return render(request, 'support/ticket_detail.html', context)


@login_required(login_url='login')
def create_ticket(request):
    """Create a support ticket (for users)"""
    if request.method == 'POST':
        subject = request.POST.get('subject')
        description = request.POST.get('description')
        category = request.POST.get('category')
        priority = request.POST.get('priority', 'MEDIUM')
        
        ticket = Ticket.objects.create(
            user=request.user,
            subject=subject,
            description=description,
            category=category,
            priority=priority
        )
        
        if 'attachment' in request.FILES:
            ticket.attachment = request.FILES['attachment']
            ticket.save()
        
        messages.success(request, f'Ticket {ticket.ticket_id} created successfully!')
        return redirect('my-tickets')
    
    context = {
        'category_choices': Ticket.CATEGORY_CHOICES,
        'priority_choices': Ticket.PRIORITY_CHOICES,
    }
    return render(request, 'support/create_ticket.html', context)


@login_required(login_url='login')
def my_tickets(request):
    """View user's own support tickets"""
    tickets = Ticket.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'tickets': tickets,
    }
    return render(request, 'support/my_tickets.html', context)


@login_required(login_url='login')
def view_ticket(request, ticket_id):
    """View user's ticket and add responses"""
    try:
        ticket = Ticket.objects.get(ticket_id=ticket_id, user=request.user)
    except Ticket.DoesNotExist:
        messages.error(request, 'Ticket not found.')
        return redirect('my-tickets')
    
    if request.method == 'POST':
        message = request.POST.get('message')
        
        TicketResponse.objects.create(
            ticket=ticket,
            responder=request.user,
            message=message,
            is_internal=False
        )
        messages.success(request, 'Response added!')
        return redirect('support-view-ticket', ticket_id=ticket_id)
    
    responses = ticket.responses.filter(is_internal=False)
    
    context = {
        'ticket': ticket,
        'responses': responses,
    }
    return render(request, 'support/view_ticket.html', context)


@login_required(login_url='login')
@require_http_methods(["GET", "POST"])
def support_profile_edit(request):
    """Create or edit support team member profile"""
    if request.user.user_type != 'SUPPORT':
        messages.error(request, 'Only support users can access this page.')
        return redirect('home')
    
    try:
        support_member = request.user.support_profile
        is_new = False
    except SupportTeamMember.DoesNotExist:
        support_member = SupportTeamMember(user=request.user)
        is_new = True
    
    if request.method == 'POST':
        form = SupportProfileForm(request.POST, instance=support_member)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            
            if is_new:
                messages.success(request, 'Support profile created successfully!')
                return redirect('support-dashboard')
            else:
                messages.success(request, 'Support profile updated successfully!')
                return redirect('support-dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SupportProfileForm(instance=support_member)
    
    context = {
        'form': form,
        'is_new': is_new,
        'title': 'Create Support Profile' if is_new else 'Edit Support Profile'
    }
    return render(request, 'support/profile_edit.html', context)
