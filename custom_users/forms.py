from django import forms
from django.forms import TextInput

from .models import Profile


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = ['profile_name', 'image', 'contact_no', 'address']

        widgets = {
            'profile_name': TextInput(attrs={'class': 'form-control'}),
            'contact_no': TextInput(attrs={'class': 'form-control'}),
            'address': TextInput(attrs={'class': 'form-control'}),
        }
