from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, EmailInput, Select

# from .models import Profile


# class UserRegisterForm(UserCreationForm):

    # GENDER = (
    #     ('MALE', 'MALE'),
    #     ('FEMALE', 'FEMALE'),
    # )
    #
    # gender = forms.ChoiceField(required=True, choices=GENDER, widget=forms.Select)
    # contact_no = forms.CharField(max_length=20, required=True, widget=forms.TextInput)
    # address = forms.CharField(max_length=250, required=True, widget=forms.TextInput)

#     class Meta:
#         model = User
#
#         fields = ['first_name','last_name', 'email', 'username', 'password1', 'password2']
#
#
# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#
#         fields = '__all__'
#         exclude = ['user', ]
#
#         widgets = {
#             'profile_name': TextInput,
#             'email': EmailInput,
#             'gender': TextInput,
#             'contact_no': TextInput,
#             'address': TextInput,
#
#         }
#
