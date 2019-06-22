from django import forms
from django.forms import TextInput, Select, Textarea, NumberInput, SelectDateWidget, TimeInput

from .models import TestOrder, Test


class TestOrderForm(forms.ModelForm):
    class Meta:
        model = TestOrder
        fields = ['client_info', 'contact_no', 'test_info', 'payment_option', 'date', 'time']

        widgets = {
            'payment_option': Select(),
            'date': SelectDateWidget(),
            'time': TimeInput(format='%H:%M', attrs={'type': 'time'}),

            # 'time': TimeInput(format='%H:%M', attrs={'placeholder': 'Select a time', 'type': 'time'})
        }


class TestAddForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['test_name', 'image', 'category', 'center', 'discount', 'price', 'active_status']

        widgets = {
            'category': Select(),
            'center': Select(),
            'active_status': Select(),
        }


