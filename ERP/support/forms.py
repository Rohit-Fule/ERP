from django import forms
from .models import SupportTeamMember


class SupportProfileForm(forms.ModelForm):
    """Form for support team member profile creation and editing"""
    
    class Meta:
        model = SupportTeamMember
        fields = [
            'employee_id', 'role', 'department', 'joining_date',
            'specialization', 'assigned_categories', 'shift', 'languages_spoken',
            'date_of_birth', 'bank_account_number', 'bank_name',
            'identity_proof', 'degree_certificate', 'certifications'
        ]
        widgets = {
            'employee_id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., SUP-2024-001'
            }),
            'role': forms.Select(attrs={
                'class': 'form-control'
            }),
            'department': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Technical Support, Customer Service'
            }),
            'joining_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'specialization': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Network Issues, Billing'
            }),
            'assigned_categories': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Technical, Billing, Account (comma-separated)'
            }),
            'shift': forms.Select(attrs={
                'class': 'form-control'
            }),
            'languages_spoken': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., English, Spanish, Hindi (comma-separated)'
            }),
            'date_of_birth': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'bank_account_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Bank account number'
            }),
            'bank_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., State Bank of India'
            }),
            'identity_proof': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.jpg,.jpeg,.png'
            }),
            'degree_certificate': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.jpg,.jpeg,.png'
            }),
            'certifications': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf'
            }),
        }
