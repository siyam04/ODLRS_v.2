from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# allauth decorator @verified_email_required
from allauth.account.decorators import verified_email_required
from allauth.account.views import SignupView, LoginView

from .models import Profile
from .forms import ProfileUpdateForm, UserLoginForm, SignupForm


class MyLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'custom_users/login.html'
    success_url = 'home'


class MySignupView(SignupView):
    form_class = SignupForm
    template_name = 'custom_users/signup.html'
    success_url = 'home'


@login_required()
def profile(request, template_name='custom_users/profile.html'):
    return render(request, template_name)


@login_required()
def profile_update(request, template_name='custom_users/profile_update.html'):

    existing_profile = get_object_or_404(Profile, user=request.user)
    profile_form = ProfileUpdateForm(instance=existing_profile)

    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=existing_profile)

        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Profile Updated for {}'.format(request.user.username), extra_tags='html_safe')
            return redirect('custom_users:profile')

    context = {
        'profile_form': profile_form,
        'existing_profile': existing_profile,
        }

    return render(request, template_name, context)



