from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import (
    ListView,
    TemplateView,
)

from tests.models import TestOrder, Test
from report_processing.models import PaymentValidation
from report_processing.forms import PaymentValidationForm, SendMessageForm

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


def admin_login(request):
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

    template = 'diagnostic_centers/admin_login.html'

    context = {'admin_login_form': admin_login_form}

    return render(request, template, context)


########################################################################################################################


def admin_dashboard(request, username=None):
    # pending_staff_tests = TestOrder.objects.filter(accepted=True, test_info__center=admin.center).order_by('-id')
    # confirmed_tests = TestOrder.objects.filter(accepted=True, test_info__center=admin.center).order_by('-id')

    admin = DiagnosticAdmin.objects.get(username=username)

    validated_orders = TestOrder.objects.filter(accepted=True, validation=True, test_info__center=admin.center)

    completed_orders = PaymentValidation.objects.filter(approved_order__payment_type='Full Payment')

    # Completed Paginator
    paginator = Paginator(completed_orders, 5)
    page = request.GET.get('page')
    completed_orders_paginator_data = paginator.get_page(page)

    paginator = Paginator(validated_orders, 5)
    page = request.GET.get('page')
    paginator_data = paginator.get_page(page)

    template = 'diagnostic_centers/admin_dashboard.html'

    context = {
        'admin': admin,
        'confirmed_tests': paginator_data,
        'completed_orders': completed_orders_paginator_data
    }

    return render(request, template, context)


########################################################################################################################


def admin_logout(request):
    # messages.success(request, 'Logged Out.', extra_tags='html_safe')
    return redirect('diagnostic_centers:admin-login')


########################################################################################################################


def staff_login(request):
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

    template = 'diagnostic_centers/staff_login.html'

    context = {'staff_login_form': staff_login_form}

    return render(request, template, context)


########################################################################################################################


def staff_dashboard(request, id=None, username=None):

    staff = DiagnosticStaff.objects.get(username=username)
    admins = DiagnosticAdmin.objects.filter(staff=staff)

    # Step 0
    pending_tests = TestOrder.objects.filter(accepted=False, order_confirmed=True, staff_check=False,
                                             test_info__center=staff.center)
    # Step 1
    confirmed_tests = TestOrder.objects.filter(accepted=True, order_confirmed=True, test_info__center=staff.center)

    # Step 4
    half_payment_orders = TestOrder.objects.filter(accepted=True, order_confirmed=True, payment_type='Half Payment',
                                                   test_info__center=staff.center)
    # Step 2 + 3
    came_for_tests = TestOrder.objects.filter(accepted=True, test_info__center=staff.center)

    # Step 5 + 6
    full_payment_orders = TestOrder.objects.filter(accepted=True, order_confirmed=True, payment_type='Full Payment',
                                                   test_info__center=staff.center)
    # Step 7
    # all_reports_query = PaymentValidation.objects.all()
    completed_orders = PaymentValidation.objects.filter(approved_order__payment_type='Full Payment')

    # Step 8
    sent_message_orders = PaymentValidation.objects.filter(approved_order__payment_type='Half Payment')

    # Pending Orders Paginator
    paginator = Paginator(pending_tests, 3)
    page = request.GET.get('page')
    pending_paginator_data = paginator.get_page(page)

    # Confirmed Orders Paginator
    paginator = Paginator(confirmed_tests, 3)
    page = request.GET.get('page')
    confirmed_paginator_data = paginator.get_page(page)

    # Half payment Orders Paginator
    paginator = Paginator(half_payment_orders, 2)
    page = request.GET.get('page')
    half_payment_paginator_data = paginator.get_page(page)

    # Came for test Paginator
    paginator = Paginator(came_for_tests, 3)
    page = request.GET.get('page')
    came_for_paginator_data = paginator.get_page(page)

    # Full payment Paginator
    paginator = Paginator(full_payment_orders, 3)
    page = request.GET.get('page')
    full_payment_paginator_data = paginator.get_page(page)

    # Completed orders Paginator
    paginator = Paginator(completed_orders, 5)
    page = request.GET.get('page')
    completed_orders_paginator_data = paginator.get_page(page)

    # Sent message orders Paginator
    paginator = Paginator(sent_message_orders, 5)
    page = request.GET.get('page')
    sent_message_orders_paginator_data = paginator.get_page(page)

    if request.method == 'POST':
        form = PaymentValidationForm(request.POST, request.FILES)

        # <!----------------------------- ERROR ------------------------------------->
        message_form = SendMessageForm(request.POST, request.FILES)

        if message_form.is_valid():
            send_message_form = message_form.save(commit=False)
            # order = TestOrder.objects.get(id=id)
            order = TestOrder.objects.get(id=id)
            order.payment_type = 'Half Payment'
            order.save()
            # send_message_form.approved_order = order.test_info.test_name
            send_message_form.send_message = order.payment_type
            send_message_form.save()
        # <!----------------------------- ERROR ------------------------------------->

        if form.is_valid():

            payment_form = form.save(commit=False)

            order = TestOrder.objects.get(id=id)
            order.validation = True
            order.save()

            payment_form.approved_order = order
            payment_form.save()

    template = 'diagnostic_centers/staff_dashboard.html'

    context = {
        'staff': staff,
        'admins': admins,

        'pending_tests': pending_paginator_data,
        'confirmed_tests': confirmed_paginator_data,
        'half_payment_orders': half_payment_paginator_data,
        'came_for_tests': came_for_paginator_data,
        'full_payment_orders': full_payment_paginator_data,
        'completed_orders': completed_orders_paginator_data,
        'sent_message_orders': sent_message_orders_paginator_data,

        'staff_username': username,
        'payment_form': PaymentValidationForm(),

    # <!----------------------------- ERROR ------------------------------------->
        'send_message_form': SendMessageForm(),
    # <!----------------------------- ERROR ------------------------------------->

    }

    return render(request, template, context)


########################################################################################################################


def staff_logout(request):
    # messages.success(request, 'Logged Out.', extra_tags='html_safe')
    return redirect('diagnostic_centers:staff-login')

########################################################################################################################


def center_details(request, id=id):
    single_center = DiagnosticCenter.objects.get(id=id)
    tests_by_center = Test.objects.filter(center__id=id)

    template = 'diagnostic_centers/center_details.html'

    context = {
        'tests_by_center': tests_by_center,
        'single_center': single_center,
    }

    return render(request, template, context)

########################################################################################################################




