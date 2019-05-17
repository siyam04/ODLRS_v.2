from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import ProfileUpdateForm
from .models import Profile


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
            return redirect('profile')

    context = {
        'profile_form': profile_form,
        }

    return render(request, template_name, context)





# @login_required()
# def user_profile(request, template_name='profile.html'):

    # messages.success(request, 'Profile Created for {}'.format(request.user.username), extra_tags='html_safe')

    # return render(request, template_name)


# def registration(request, template_name='accounts/registration.html'):
#
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#
#             form_username = form.cleaned_data.get('username')
#             form_password = form.cleaned_data.get('password2')
#
#             messages.success(request, 'Registration Successful! for {}'.format(form_username), extra_tags='html_safe')
#
#             user = authenticate(username=form_username, password=form_password)
#             login(request, user)
#
#             return redirect('home')
#
#     else:
#         form = UserRegisterForm()
#
#     context = {'form': form}
#
#     return render(request, template_name, context)




# from allauth.account.views import SignupView, LoginView, PasswordResetView
#
# class MySignupView(SignupView):
#     template_name = 'signup.html'
#
# class MyLoginView(LoginView):
#     template_name = 'login.html'
#
# class MyPasswordResetView(PasswordResetView):
#     template_name = 'password_reset.html'
#
# urlpatterns = [
#     url(r'^accounts/login', MyLoginView.as_view(), name='account_login'),
#     url(r'^accounts/signup', MySignupView.as_view(), name='account_signup'),
#     url(r'^accounts/password_reset', MyPasswordResetView.as_view(), name='account_reset_password'),
# ]

