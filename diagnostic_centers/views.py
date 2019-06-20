from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import (
    ListView,
    TemplateView,
)

from .models import DiagnosticCenter, DiagnosticAdmin, DiagnosticStaff
from .forms import AdminLoginForm, StaffLoginForm

########################################################################################################################


def search_paginator(request):
    Centers = DiagnosticCenter.objects.all()

    query = request.GET.get('q')
    if query:
        Centers = Centers.filter(
            Q(name__icontains=query) |
            Q(website__icontains=query)
        )
        print(Centers)

    paginator = Paginator(Centers, 2) 
    page = request.GET.get('page')
    all_centers = paginator.get_page(page)

    context = {"Centers": all_centers,}
    template_name = 'diagnostic_centers/all_centers.html'

    return render(request, template_name, context)


########################################################################################################################


def admin_login(request, template_name='diagnostic_centers/admin_login.html'):
    admin_login_form = AdminLoginForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            DiagnosticAdmin.objects.get(username=username, password=password)
            messages.success(request, 'Login Successful for {}'.format(username), extra_tags='html_safe')
            return redirect('diagnostic_centers:admin-dashboard', username)

        except DiagnosticAdmin.DoesNotExist:
            return redirect('diagnostic_centers:admin-login')

    context = {'admin_login_form': admin_login_form}

    return render(request, template_name, context)


########################################################################################################################


def admin_dashboard(request, username=None, template_name='diagnostic_centers/admin_dashboard.html'):
    admin = DiagnosticAdmin.objects.get(username=username)

    context = {'admin': admin}

    return render(request, template_name, context)


########################################################################################################################


def admin_logout(request):
    # messages.success(request, 'Logged Out.', extra_tags='html_safe')
    return redirect('diagnostic_centers:admin-login')


########################################################################################################################


def staff_login(request, template_name='diagnostic_centers/staff_login.html'):
    staff_login_form = StaffLoginForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            DiagnosticStaff.objects.get(username=username, password=password)
            messages.success(request, 'Login Successful for {}'.format(username), extra_tags='html_safe')
            return redirect('diagnostic_centers:staff-dashboard', username)

        except DiagnosticStaff.DoesNotExist:
            return redirect('diagnostic_centers:staff-login')

    context = {'staff_login_form': staff_login_form}

    return render(request, template_name, context)


########################################################################################################################


def staff_dashboard(request, username=None, template_name='diagnostic_centers/staff_dashboard.html'):
    staff = DiagnosticStaff.objects.get(username=username)
    admins = DiagnosticAdmin.objects.filter(staff=staff)

    context = {
        'staff': staff,
        'admins': admins,
    }

    return render(request, template_name, context)


########################################################################################################################


def staff_logout(request):
    # messages.success(request, 'Logged Out.', extra_tags='html_safe')
    return redirect('diagnostic_centers:staff-login')


