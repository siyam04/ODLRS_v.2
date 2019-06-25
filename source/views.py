from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q

from tests.models import Test, TestCategory


def home(request):
    paginator_dataset = Test.objects.all()
    all_category = TestCategory.objects.all()

    query = request.GET.get('q')

    if query:
        paginator_dataset = paginator_dataset.filter(Q(test_name__icontains=query)).distinct()

    paginator = Paginator(paginator_dataset, 8)
    page = request.GET.get('page')

    all_tests = paginator.get_page(page)

    context = {
        'paginator_dataset': all_tests,
        'all_category': all_category,
    }

    template_name = 'home.html'

    return render(request, template_name, context)

