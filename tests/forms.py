from django import forms
from django.forms import TextInput, Select, Textarea, NumberInput, SelectDateWidget, TimeInput

from .models import TestOrder


class TestOrderForm(forms.ModelForm):
    class Meta:
        model = TestOrder
        fields = ['client_info', 'test_info', 'payment_option', 'date', 'time']

        widgets = {
            'payment_option': Select(),
            'date': SelectDateWidget(),
            'time': TimeInput(format='%H:%M', attrs={'type': 'time'}),

            # 'time': TimeInput(format='%H:%M', attrs={'placeholder': 'Select a time', 'type': 'time'})
        }




