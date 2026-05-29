from django import forms
from .models import Organization


class OrganizationProfileForm(forms.ModelForm):
    """Form for organization profile creation and editing"""
    
    class Meta:
        model = Organization
        fields = [
            'organization_name', 'registration_number', 'website', 'establishment_year',
            'description', 'logo', 'banner', 'principal_name', 'principal_email', 'principal_phone',
            'contact_email', 'contact_phone',
            'accreditation_type', 'accreditation_number', 'university_affiliation', 'gstin',
            'headquarters_address', 'headquarters_city', 'headquarters_state',
            'headquarters_postal_code', 'headquarters_country',
            'registration_certificate', 'accreditation_certificate', 'license'
        ]
        widgets = {
            'organization_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., University of Excellence'
            }),
            'registration_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., REG-2024-001'
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://www.example.edu'
            }),
            'establishment_year': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'min': '1900',
                'max': '2024'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe your organization...'
            }),
            'logo': forms.FileInput(attrs={'class': 'form-control'}),
            'banner': forms.FileInput(attrs={'class': 'form-control'}),
            'principal_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Principal/Director name'
            }),
            'principal_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'principal@example.edu'
            }),
            'principal_phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+1 (555) 000-0000'
            }),
            'contact_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'contact@example.edu'
            }),
            'contact_phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+1 (555) 000-0000'
            }),
            'accreditation_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'accreditation_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Accreditation number'
            }),
            'university_affiliation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Affiliated with (if applicable)'
            }),
            'gstin': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'GSTIN (if applicable)'
            }),
            'headquarters_address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '123 Main Street'
            }),
            'headquarters_city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City'
            }),
            'headquarters_state': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'State/Province'
            }),
            'headquarters_postal_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Postal Code'
            }),
            'headquarters_country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Country'
            }),
            'registration_certificate': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.jpg,.jpeg,.png'
            }),
            'accreditation_certificate': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.jpg,.jpeg,.png'
            }),
            'license': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.jpg,.jpeg,.png'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'
