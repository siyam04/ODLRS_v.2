from django import forms

from .models import DiagnosticAdmin, DiagnosticStaff, DiagnosticCenter


class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = DiagnosticAdmin
        fields = ['username', 'password']


class StaffLoginForm(forms.ModelForm):
    class Meta:
        model = DiagnosticStaff
        fields = ['username', 'password']


