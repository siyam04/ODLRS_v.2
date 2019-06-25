from django import forms
from django.forms import TextInput

from .models import DiagnosticAdmin, DiagnosticStaff, DiagnosticCenter


class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = DiagnosticAdmin

        fields = ['username', 'password']

        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'password': TextInput(attrs={'class': 'form-control'}),
        }


class StaffLoginForm(forms.ModelForm):
    class Meta:
        model = DiagnosticStaff

        fields = ['username', 'password']

        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'password': TextInput(attrs={'class': 'form-control'}),
        }




