from django import forms
from phase1.models import Advocates
from django.forms import ModelForm


class AdvocateRegistrationForm(forms.ModelForm):
    class Meta:
        model = Advocates
        fields = ('name', 'email', 'phone', 'enrollment_id', 'address', 'id_image')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Name', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Email', 'required': True}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone', 'placeholder': 'Phone Number', 'required': True}),
            'enrollment_id': forms.TextInput(attrs={'class': 'form-control', 'id': 'enrollment', 'placeholder': 'Enrollment ID', 'required': True}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Address', 'required': True}),
            'id_image': forms.FileInput(attrs={'class': 'form-control', 'id': 'subject', 'placeholder': 'Subject', 'required': True}),
        }
        labels = {
            'name': 'Name',
            'email': 'Email',
            'phone': 'Phone Number',
            'enrollment_id': 'Enrollment ID',
            'address': 'Address',
            'id_image': 'ID Card',
        }


