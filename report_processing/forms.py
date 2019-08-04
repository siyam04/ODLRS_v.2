from django import forms
from django.forms import TextInput, FileInput, Select, SelectDateWidget

# from tests.models import TestOrder

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


# class CompleteDuePaymentForm(forms.ModelForm):
#     class Meta:
#         model = TestOrder
#
#         fields = '__all__'
#
#         exclude = ['client_info', 'test_info', 'order_created_at', 'staff_check', 'admin_approve',
#                    'accepted', 'validation', 'order_confirmed', 'came_for_test', 'booked_time_slot',
#                    'booked_date']
#
#         widgets = {
#             'client_info': Select(attrs={'class': 'form-control'}),
#             'contact_no': TextInput(attrs={'class': 'form-control'}),
#             'email': TextInput(attrs={'class': 'form-control'}),
#             'address': TextInput(attrs={'class': 'form-control'}),
#             'test_info': Select(attrs={'class': 'form-control'}),
#             'payment_type': Select(attrs={'class': 'form-control'}),
#             'payment_method': Select(attrs={'class': 'form-control'}),
            # 'booked_time_slot': Select(attrs={'class': 'form-control'}),
            # 'booked_date': SelectDateWidget(attrs={'class': 'form-control'}),

            # 'time': TimeInput(format='%H:%M', attrs={'type': 'time', 'class': 'form-control'}),
            # 'date': SelectDateWidget(attrs={'class': 'form-control'}),
        # }





