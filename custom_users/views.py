from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# from .forms import UserRegisterForm, ProfileForm


# @login_required()
# def user_profile(request, template_name='profile.html'):

    # messages.success(request, 'Profile Created for {}'.format(request.user.username), extra_tags='html_safe')

    # return render(request, template_name)


@login_required
def profile(request):
    return render(request, 'profile.html')


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




