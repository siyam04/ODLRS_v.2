from django import forms
from django.forms import TextInput, FileInput

from .models import PaymentValidation


class PaymentValidationForm(forms.ModelForm):
    class Meta:
        model = PaymentValidation

        fields = '__all__'
        exclude = ['approved_order', ]

        widgets = {
            'upload_report': FileInput(attrs={'class': 'form-control'}),
            'send_message': TextInput(attrs={'class': 'form-control'}),
        }


# class SendMessageForm(forms.ModelForm):
#     class Meta:
#         model = PaymentValidation
#
#         fields = ['send_message']
#         exclude = ['approved_order', 'upload_report', ]
#
#         widgets = {'send_message': TextInput(attrs={'class': 'form-control'}),}

