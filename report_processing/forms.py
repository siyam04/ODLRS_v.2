from django import forms
from django.forms import TextInput, FileInput

from .models import PaymentValidation


class PaymentValidationForm(forms.ModelForm):
    class Meta:
        model = PaymentValidation

        fields = '__all__'
        exclude = ['approved_order']

        widgets = {'upload_report': FileInput(attrs={'class': 'form-control'}),}