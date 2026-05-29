from django import forms
from .models import Student
from organizations.models import Organization


class StudentProfileForm(forms.ModelForm):
    """Form for student profile creation and editing"""
    
    organization = forms.ModelChoiceField(
        queryset=Organization.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
        }),
        label='Organization/Institution'
    )
    
    class Meta:
        model = Student
        fields = [
            'organization', 'enrollment_number', 'roll_number', 'program', 'current_year',
            'semester', 'batch_year', 'admission_date', 'date_of_birth', 
            'parent_name', 'parent_phone', 'emergency_contact_name', 'emergency_contact_phone',
            'enrollment_date', 'expected_graduation_date',
            'admission_letter', 'identity_proof', 'certificate_10th', 'certificate_12th', 'medical_certificate'
        ]
        widgets = {
            'organization': forms.Select(attrs={'class': 'form-control'}),
            'enrollment_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., ENR-2024-001'
            }),
            'roll_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., CS-101'
            }),
            'program': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Bachelor of Science in Computer Science'
            }),
            'current_year': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'min': '1',
                'max': '8'
            }),
            'semester': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'min': '1',
                'max': '8'
            }),
            'batch_year': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'min': '2000'
            }),
            'admission_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'date_of_birth': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'parent_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Parent/Guardian full name'
            }),
            'parent_phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+1 (555) 000-0000'
            }),
            'emergency_contact_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Emergency contact name'
            }),
            'emergency_contact_phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+1 (555) 000-0000'
            }),
            'enrollment_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'expected_graduation_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'admission_letter': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.doc,.docx'
            }),
            'identity_proof': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.jpg,.jpeg,.png'
            }),
            'certificate_10th': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.jpg,.jpeg,.png'
            }),
            'certificate_12th': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.jpg,.jpeg,.png'
            }),
            'medical_certificate': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.jpg,.jpeg,.png'
            }),
        }
        widgets = {
            'enrollment_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., ENR-2024-001'
            }),
            'roll_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., CS-101'
            }),
            'program': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Bachelor of Science in Computer Science'
            }),
            'semester': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'min': '1',
                'max': '8'
            }),
            'batch_year': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'min': '2000'
            }),
            'enrollment_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'expected_graduation_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }
