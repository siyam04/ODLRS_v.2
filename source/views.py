from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q

from tests.models import Test, TestCategory


# def home(request, template_name='home.html'):
#     all_test_list = Test.objects.all()
#
#     context = {'all_test_list': all_test_list}
#
#     return render(request, template_name, context)


def home(request):
    T = Test.objects.all()
    all_category = TestCategory.objects.all()

    query = request.GET.get('q')

    if query:
        T = T.filter(Q(test_name__icontains=query)).distinct()

    paginator = Paginator(T, 2)
    page = request.GET.get('page')

    all_tests = paginator.get_page(page)

    context = {
        'T': all_tests,
        'all_category': all_category,
    }

    template_name = 'home.html'

    return render(request, template_name, context)

