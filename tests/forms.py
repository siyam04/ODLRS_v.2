from django import forms
from django.forms import TextInput, Select, SelectDateWidget, TimeInput, DateInput

from .models import TestOrder, Test


class TestOrderForm(forms.ModelForm):
    class Meta:
        model = TestOrder
        # fields = ['client_info', 'contact_no', 'email', 'address', 'test_info', 'payment_type', 'payment_method',
        #
        #           'booked_time_slot', 'booked_date']

        fields = '__all__'

        exclude = ['client_info', 'test_info', 'order_created_at', 'staff_check', 'admin_approve', 'accepted', 'validation']

        widgets = {
            'client_info': Select(attrs={'class': 'form-control'}),
            'contact_no': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            'address': TextInput(attrs={'class': 'form-control'}),
            'test_info': Select(attrs={'class': 'form-control'}),
            'payment_type': Select(attrs={'class': 'form-control'}),
            'payment_method': Select(attrs={'class': 'form-control'}),
            'booked_time_slot': Select(attrs={'class': 'form-control'}),
            'booked_date': SelectDateWidget(attrs={'class': 'form-control'}),

            # 'time': TimeInput(format='%H:%M', attrs={'type': 'time', 'class': 'form-control'}),
            # 'date': SelectDateWidget(attrs={'class': 'form-control'}),
        }


class TestAddForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['test_name', 'image', 'category', 'discount', 'price', 'active_status']
        exclude = ['center', ]

        widgets = {
            'test_name': TextInput(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'}),
            # 'center': Select(attrs={'class': 'form-control'}),
            'discount': TextInput(attrs={'class': 'form-control'}),
            'price': TextInput(attrs={'class': 'form-control'}),
            'active_status': Select(attrs={'class': 'form-control'}),
        }


