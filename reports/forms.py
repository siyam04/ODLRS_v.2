from django import forms
from django.forms import (

    TextInput,
    Select,
    SelectDateWidget,
    CheckboxInput,
    DateTimeInput,
    TimeInput,
    DateInput,
    SplitDateTimeWidget,
)

from .models import OrderValidation


class OrderValidationForm(forms.ModelForm):
    class Meta:
        model = OrderValidation
        fields = ['approved_order_by_client', 'payment_status', 'confirmed_by_staff', 'confirmation_datetime']

        widgets = {
            'approved_order_by_client': Select(attrs={'class': 'form-control'}),
            'payment_status': Select(attrs={'class': 'form-control'}),
            'confirmed_by_staff': CheckboxInput(attrs={'class': 'form-control'}),
            'confirmation_datetime': SplitDateTimeWidget(date_format='%d %B %Y', time_format='%I:%M %p',
                                                         attrs={'class': 'form-control'}),
        }


