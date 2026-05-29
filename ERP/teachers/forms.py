from django import forms
from .models import Teacher


class TeacherProfileForm(forms.ModelForm):
    """Form for teacher profile creation and editing"""
    
    class Meta:
        model = Teacher
        fields = [
            'employee_id', 'department', 'designation', 'joining_date',
            'qualification', 'specialization', 'experience_years',
            'date_of_birth', 'bank_account_number', 'bank_name', 'pan_number',
            'degree_certificate', 'identity_proof', 'teaching_license',
            'experience_certificate', 'research_publications'
        ]
        widgets = {
            'employee_id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., EMP-2024-001'
            }),
            'department': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Computer Science'
            }),
            'designation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Assistant Professor'
            }),
            'joining_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'qualification': forms.Select(attrs={
                'class': 'form-control'
            }),
            'specialization': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Machine Learning, Database Systems'
            }),
            'experience_years': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'min': '0'
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
            'pan_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'PAN number'
            }),
            'degree_certificate': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.jpg,.jpeg,.png'
            }),
            'identity_proof': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.jpg,.jpeg,.png'
            }),
            'teaching_license': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.jpg,.jpeg,.png'
            }),
            'experience_certificate': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.jpg,.jpeg,.png'
            }),
            'research_publications': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf'
            }),
        }
