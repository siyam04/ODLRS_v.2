from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import (
    Paginator,
    PageNotAnInteger,
    EmptyPage
)

from diagnostic_centers.models import DiagnosticCenter


def home(request):
    queryset_list = DiagnosticCenter.objects.all()

    # Searching
    query = request.GET.get('q', None)
    if query:
        queryset_list = queryset_list.filter(
            Q(name__icontains=query) |
            Q(website__icontains=query)
        ).distinct()  # distinct used for not the duplicate search

    # Paginator shows 'n' number of contents per page
    paginator = Paginator(queryset_list, 5)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    template = 'home.html'
    context = {
        'all_centers': queryset,
        'queryset_list': queryset_list,
        'page_request_var': page_request_var,
        'page': page,
    }

    return render(request, template, context)





