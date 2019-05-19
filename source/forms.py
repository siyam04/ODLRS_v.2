
from django import forms
from allauth.account.views import SignupForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(LoginForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control col-sm-9'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control col-sm-9'
    }))

    class Meta:
        model=User
        fields=('username','password')



class SignupForm(UserCreationForm):
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control col-sm-9'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control col-sm-9'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control col-sm-9'
    }))


    class Meta:
        model=User
        fields=('email','password1','password2')
