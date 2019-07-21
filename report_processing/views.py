from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from custom_users.models import Profile

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

    template = 'report_processing/single_report_details.html'

    context = {'report_details': report_details}

    return render(request, template, context)

########################################################################################################################


