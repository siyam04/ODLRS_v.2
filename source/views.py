from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from allauth.account.views import SignupView,LoginView
from .forms import LoginForm,SignupForm

class Home(TemplateView):
    template_name = 'home.html'


class MyLoginView(LoginView):
    form_class=LoginForm
    template_name='login.html'

class MySignupView(SignupView):
    form_class=SignupForm
    template_name='signup.html'



