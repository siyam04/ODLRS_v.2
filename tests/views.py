from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from custom_users.models import Profile

from .models import Test, TestCategory, TestOrder
from .forms import TestOrderForm, TestAddForm

########################################################################################


def all_tests(request, template_name='tests/all_tests.html'):
    all_test_list = Test.objects.all().order_by('-id')

    context = {'all_test_list': all_test_list}

    return render(request, template_name, context)

########################################################################################


def test_categories(request, template_name='tests/categories.html'):
    categories = TestCategory.objects.all().order_by('-id')

    context = {'categories': categories}

    return render(request, template_name, context)

########################################################################################


def categorise_tests(request, id=None):
    filtered_tests = Test.objects.filter(category__id=id)

    template = 'tests/categorise_tests.html'
    context = {'filtered_tests': filtered_tests}

    return render(request, template, context)

########################################################################################


def test_details(request, id=id):
    single_test_details = Test.objects.get(id=id)

    template = 'tests/test_details.html'
    context = {'single_test_details': single_test_details}

    # return redirect('tests:test-details', id)
    return render(request, template, context)

########################################################################################


@login_required
def test_order(request, id=None):

    try:
        current_profile = Profile.objects.get(user=request.user)
        current_test = Test.objects.get(id=id).order_by('-id')

        initial_data = {
            'client_info': current_profile,
            'test_info': current_test,
        }

    except:
        return redirect('account_login')

    if request.method == 'POST':
        test_order_form = TestOrderForm(request.POST)

        if test_order_form.is_valid():
            order = test_order_form.save(commit=False)
            # order.client_info = current_profile
            # order.test_info = current_test
            order.save()
            return redirect('tests:order-details', id=order.id)

    context = {
        'test_order_form': TestOrderForm(initial=initial_data),
    }

    template = 'tests/order.html'

    return render(request, template, context)

########################################################################################


def order_details_info(request, id=None):
    order_details = TestOrder.objects.get(id=id)

    template = 'tests/order_details.html'

    context = {
        'order_details': order_details,
    }

    return render(request, template, context)

########################################################################################


def staff_approved(request, id=None):
    staff_order_detail = TestOrder.objects.get(id=id)
    staff_order_detail.accepted = True
    staff_order_detail.staff_check = True
    staff_order_detail.save()

    template = 'tests/order_details.html'

    context = {
        'order_details': staff_order_detail,
    }

    return render(request, template, context)

########################################################################################


def staff_rejected(request, id=None):
    staff_order_detail = TestOrder.objects.get(id=id)
    staff_order_detail.accepted = False
    staff_order_detail.staff_check = True
    staff_order_detail.save()

    template = 'tests/order_details.html'

    context = {
        'order_details': staff_order_detail,
    }

    return render(request, template, context)

########################################################################################


def add_test_by_staff(request):
    if request.method == 'POST':
        test_add_form = TestAddForm(request.POST)

        if test_add_form.is_valid():
            test_add_form.save()
            return redirect('tests:all-tests-list-staff')

    else:
        test_add_form = TestAddForm()

    template = 'tests/add_test.html'
    context = {'test_add_form': test_add_form}

    return render(request, template, context)

########################################################################################


def all_tests_list_for_staff(request, template_name='tests/all_tests_list_for_staff.html'):
    all_added_tests = Test.objects.all().order_by('-id')

    context = {'all_added_tests': all_added_tests}

    return render(request, template_name, context)

########################################################################################
