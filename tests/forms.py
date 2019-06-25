from django import forms
from django.forms import TextInput, Select, Textarea, NumberInput, SelectDateWidget, TimeInput

from .models import TestOrder, Test


class TestOrderForm(forms.ModelForm):
    class Meta:
        model = TestOrder
        fields = ['client_info', 'contact_no', 'email', 'address', 'test_info', 'payment_option', 'date', 'time']

        widgets = {
            'payment_option': Select(attrs={'class': 'form-control'}),
            'date': SelectDateWidget(attrs={'class': 'form-control'}),
            'time': TimeInput(format='%H:%M', attrs={'type': 'time'}),
        }


class TestAddForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['test_name', 'image', 'category', 'center', 'discount', 'price', 'active_status']

        widgets = {
            'active_status': Select(attrs={'class': 'form-control'}),
        }


