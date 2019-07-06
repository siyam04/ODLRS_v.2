from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import (
    ListView,
    TemplateView,
)

from tests.models import TestOrder

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

    paginator = Paginator(Centers, 8)
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
            # messages.success(request, 'Login Successful for {}'.format(username), extra_tags='html_safe')
            return redirect('diagnostic_centers:admin-dashboard', username)

        except DiagnosticAdmin.DoesNotExist:
            return redirect('diagnostic_centers:admin-login')

    context = {'admin_login_form': admin_login_form}

    return render(request, template_name, context)


########################################################################################################################


def admin_dashboard(request, username=None, template_name='diagnostic_centers/admin_dashboard.html'):
    admin = DiagnosticAdmin.objects.get(username=username)

    # pending_staff_tests = TestOrder.objects.filter(accepted=True, test_info__center=admin.center).order_by('-id')
    confirmed_tests = TestOrder.objects.filter(accepted=True, test_info__center=admin.center).order_by('-id')

    paginator = Paginator(confirmed_tests, 5)
    page = request.GET.get('page')
    paginator_data = paginator.get_page(page)

    context = {
        'admin': admin,
        'confirmed_tests': paginator_data,
    }

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
            # messages.success(request, 'Login Successful for {}'.format(username), extra_tags='html_safe')
            return redirect('diagnostic_centers:staff-dashboard', username)

        except DiagnosticStaff.DoesNotExist:
            return redirect('diagnostic_centers:staff-login')

    context = {'staff_login_form': staff_login_form}

    return render(request, template_name, context)


########################################################################################################################


def staff_dashboard(request, username=None, template_name='diagnostic_centers/staff_dashboard.html'):
    staff = DiagnosticStaff.objects.get(username=username)
    admins = DiagnosticAdmin.objects.filter(staff=staff)

    pending_tests = TestOrder.objects.filter(test_info__center=staff.center).order_by('-id')

    # for active tests like admin_dashboard
    confirmed_tests = TestOrder.objects.filter(accepted=True, test_info__center=staff.center).order_by('-id')
    ##

    # Pending Orders Paginator
    paginator = Paginator(pending_tests, 5)
    page = request.GET.get('page')
    pending_paginator_data = paginator.get_page(page)

    # Confirmed Orders Paginator
    paginator = Paginator(confirmed_tests, 3)
    page = request.GET.get('page')
    confirmed_paginator_data = paginator.get_page(page)

    context = {
        'staff': staff,
        'admins': admins,
        'pending_tests': pending_paginator_data,
        'confirmed_tests': confirmed_paginator_data,
    }

    return render(request, template_name, context)


########################################################################################################################


def staff_logout(request):
    # messages.success(request, 'Logged Out.', extra_tags='html_safe')
    return redirect('diagnostic_centers:staff-login')


