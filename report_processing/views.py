from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from custom_users.models import Profile
from tests.models import Test, TestOrder

from .models import PaymentValidation
from .forms import PaymentValidationForm

########################################################################################################################


def all_reports(request):
    all_reports_query = PaymentValidation.objects.all()

    # All reports Paginator
    paginator = Paginator(all_reports_query, 5)
    page = request.GET.get('page')
    all_reports_paginator = paginator.get_page(page)

    template = 'report_processing/all_reports.html'

    context = {'all_reports_query': all_reports_paginator}

    return render(request, template, context)

########################################################################################################################


def single_report_details(request, id=None):
    report_details = PaymentValidation.objects.get(id=id)

    total_price = int(report_details.approved_order.test_info.price - report_details.approved_order.test_info.discount)

    due_price = int(
        (report_details.approved_order.test_info.price - report_details.approved_order.test_info.discount) / 2)

    template = 'report_processing/single_report_details.html'

    context = {
        'report_details': report_details,
        'total_price': total_price,
        'due_price': due_price,
    }

    return render(request, template, context)

########################################################################################################################


# def complete_due_payment(request, id=None):
#     existing_order = TestOrder.objects.get(id=id)
#     complete_due_payment_form = CompleteDuePaymentForm(request.POST or None, instance=existing_order)
#
#     email = existing_order.client_info.user.email
#     # contact_no = existing_order.approved_order.client_info.address
#     # address = current_profile.address
#
#     initial_data = {
#         'email': email,
#         # 'contact_no': contact_no,
#         # 'address': address
#     }
#
#     if request.method == 'POST':
#         if complete_due_payment_form.is_valid():
#             complete_due_payment_form.save()
#             return redirect('tests:order-details', id)
#
#     template = 'report_processing/complete_due_payment.html'
#
#     context = {
#         'complete_due_payment_form': CompleteDuePaymentForm(initial=initial_data),
#         'existing_order': existing_order,
#     }
#
#     return render(request, template, context)
