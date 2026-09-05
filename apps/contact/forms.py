"""
Django form for the contact page template rendering.
"""
from django import forms
from .models import ContactSubmission


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your Full Name',
                'class': 'form-input',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'your@email.com',
                'class': 'form-input',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': '+91 98765 43210 (optional)',
                'class': 'form-input',
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'e.g. Corporate Law Consultation',
                'class': 'form-input',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Please describe your legal matter briefly...',
                'rows': 6,
                'class': 'form-input',
            }),
        }
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'subject': 'Subject',
            'message': 'Your Message',
        }
