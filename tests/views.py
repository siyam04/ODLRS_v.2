from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages

from custom_users.models import Profile
from diagnostic_centers.models import DiagnosticAdmin, DiagnosticStaff, DiagnosticCenter

from .models import Test, TestCategory, TestOrder
from .forms import TestOrderForm, TestAddForm, CategoryAddForm


########################################################################################


def all_tests(request, template_name='tests/all_tests.html'):
    all_test_list = Test.objects.all().order_by('-id')

    query = request.GET.get('q')

    if query:
        all_test_list = all_test_list.filter(Q(test_name__icontains=query)).distinct()

    paginator = Paginator(all_test_list, 12)
    page = request.GET.get('page')
    all_test_paginator_data = paginator.get_page(page)

    context = {
        'all_test_list': all_test_list,
        'all_test_paginator_data': all_test_paginator_data,
    }

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

    return render(request, template, context)

########################################################################################


@login_required
def test_order(request, id=None):
    try:
        current_profile = Profile.objects.get(user=request.user)
        email = current_profile.user.email
        contact_no = current_profile.contact_no
        address = current_profile.address
        initial_data = {
            'email':email,
            'contact_no': contact_no,
            'address':address
        }
    except:
        return redirect('account_login')
    if request.method == 'POST':
        test_order_form = TestOrderForm(request.POST)
        if test_order_form.is_valid():
            order = test_order_form.save(commit=False)
            order.client_info = Profile.objects.get(user=request.user)
            order.test_info = Test.objects.get(id=id)
            order.save()
            return redirect('tests:order-details', id=order.id)
    context = {
        'test_order_form': TestOrderForm(initial=initial_data),
        'test_id': id,
    }
    template = 'tests/order.html'
    return render(request, template, context)

########################################################################################


def order_details_info(request, id=None):
    order_details = TestOrder.objects.get(id=id)

    total_price = int(order_details.test_info.price - order_details.test_info.discount)

    template = 'tests/order_details.html'

    context = {
        'order_details': order_details,
        'total_price': total_price,
    }

    return render(request, template, context)

########################################################################################


def staff_approved(request, id=None, username=None):
    staff_order_detail = TestOrder.objects.get(id=id)
    staff_order_detail.accepted = True
    staff_order_detail.staff_check = True
    staff_order_detail.save()

    return redirect('diagnostic_centers:staff-dashboard', username=username)

########################################################################################


def staff_rejected(request, id=None, username=None):
    staff_order_detail = TestOrder.objects.get(id=id)
    staff_order_detail.accepted = False
    staff_order_detail.staff_check = True
    staff_order_detail.save()

    return redirect('diagnostic_centers:staff-dashboard', username=username)


########################################################################################


def add_test_by_admin(request, username=None):
    if request.method == 'POST':
        test_add_form = TestAddForm(request.POST)

        if test_add_form.is_valid():
            add_test = test_add_form.save(commit=False)

            admin = DiagnosticAdmin.objects.get(username=username)
            add_test.center = DiagnosticCenter.objects.get(id=admin.center.id)

            add_test.save()

            return redirect('tests:added-tests-list-staff-admin', username)

    else:
        test_add_form = TestAddForm()

    template = 'tests/add_test.html'
    context = {'test_add_form': test_add_form}

    return render(request, template, context)

########################################################################################


def add_category_by_admin(request, username=None):
    if request.method == 'POST':
        category_add_form = CategoryAddForm(request.POST)

        if category_add_form.is_valid():
            add_category = category_add_form.save(commit=False)

            admin = DiagnosticAdmin.objects.get(username=username)
            add_category.center = DiagnosticCenter.objects.get(id=admin.center.id)

            add_category.save()

            return redirect('tests:filtered-categories-by-admin', username)

    else:
        category_add_form = CategoryAddForm()

    template = 'tests/add_category.html'
    context = {'category_add_form': category_add_form}

    return render(request, template, context)

########################################################################################


def edit_category(request, id=None, username=None):
    category_query = TestCategory.objects.get(id=id)
    edit_form = CategoryAddForm(request.POST or None, instance=category_query)

    if request.method == 'POST':
        if edit_form.is_valid():
            edited = edit_form.save(commit=False)

            admin = DiagnosticAdmin.objects.get(username=username)
            edited.center = DiagnosticCenter.objects.get(id=admin.center.id)

            edited.save()

            return redirect('tests:filtered-categories-by-admin', username)

    template = 'tests/edit_category.html'

    context = {'edit_form': edit_form}

    return render(request, template, context)

########################################################################################


def delete_category(request, id=None, username=None):
    category_object = TestCategory.objects.get(id=id)
    admin = DiagnosticAdmin.objects.get(username=username)

    category_object.center = DiagnosticCenter.objects.get(id=admin.center.id)

    if category_object.center is not None:
        category_object.delete()

    return redirect('tests:filtered-categories-by-admin', username)

########################################################################################


def filtered_categories_by_admin(request, username=None):
    admin = DiagnosticAdmin.objects.get(username=username)
    # staff = DiagnosticStaff.objects.filter(username=username)

    added_categories_admin = TestCategory.objects.filter(center__center_admins=admin)
    # categories_staff = TestCategory.objects.filter(center__center_staffs=staff)

    template = 'tests/filtered_categories_admin.html'

    context = {
        'added_categories_admin': added_categories_admin,
        'admin': admin,
        # 'categories_staff': categories_staff,
        # 'staff': staff,
    }

    return render(request, template, context)

########################################################################################


def filtered_categories_for_staff(request, username=None):
    staff = DiagnosticStaff.objects.get(username=username)

    categories_staff = TestCategory.objects.filter(center__center_staffs=staff)

    template = 'tests/filtered_categories_staff.html'

    context = {
        'categories_staff': categories_staff,
        'staff': staff,
    }

    return render(request, template, context)

########################################################################################


def all_tests_list_for_staff(request, username):
    # all_added_tests = Test.objects.all().order_by('-id')
    staff = DiagnosticStaff.objects.get(username=username)

    staff_filtered_tests = Test.objects.filter(center__center_staffs=staff)

    # All added tests Paginator
    paginator = Paginator(staff_filtered_tests, 20)
    page = request.GET.get('page')
    all_added_tests_paginator_data = paginator.get_page(page)

    template = 'tests/all_tests_list_for_staff.html'
    context = {
        'all_added_tests': all_added_tests_paginator_data,
        'staff': staff,
    }

    return render(request, template, context)

########################################################################################


def added_tests_list_for_staff_admin(request, username=None):

    admin = DiagnosticAdmin.objects.get(username=username)
    # staffs = DiagnosticStaff.objects.filter(username=username)

    added_tests = Test.objects.filter(center__center_admins=admin)

    # staffs_by_center = Test.objects.filter(center__center_staffs=staffs)

    # All added tests Paginator
    paginator = Paginator(added_tests, 20)
    page = request.GET.get('page')
    added_tests_paginator_data = paginator.get_page(page)

    template = 'tests/added_tests_list_for_staff_admin.html'

    context = {
        'all_added_tests': added_tests_paginator_data,
        'admin': admin,
        # 'staffs': staffs,
        # 'staffs_by_center': staffs_by_center,
    }

    return render(request, template, context)

########################################################################################


def delete_test(request, id=None, username=None):
    test_object = Test.objects.get(id=id)
    admin = DiagnosticAdmin.objects.get(username=username)

    test_object.center = DiagnosticCenter.objects.get(id=admin.center.id)

    if test_object.center is not None:
        test_object.delete()

    return redirect('tests:added-tests-list-staff-admin', username)

########################################################################################


def edit_test(request, id=None, username=None):
    test_query = Test.objects.get(id=id)
    edit_form = TestAddForm(request.POST or None, instance=test_query)

    if request.method == 'POST':
        if edit_form.is_valid():
            edited = edit_form.save(commit=False)

            admin = DiagnosticAdmin.objects.get(username=username)
            edited.center = DiagnosticCenter.objects.get(id=admin.center.id)

            edited.save()

            return redirect('tests:added-tests-list-staff-admin', username)
            # return added_tests_list_for_staff_admin(request)

    context = {'edit_form': edit_form}
    template = 'tests/edit_test.html'

    return render(request, template, context)

########################################################################################


def confirm_payment_message(request, id=None, username=None):
    order_details = TestOrder.objects.get(id=id)

    order_details.order_confirmed = True
    order_details.save()

    total_price = int(order_details.test_info.price - order_details.test_info.discount)

    template = 'tests/confirm_payment_message.html'
    context = {
        'order_details': order_details,
        'total_price': total_price,
        'staff_username': username,
    }

    return render(request, template, context)

########################################################################################


def came_for_test(request, id=None, username=None):
    staff_order_detail = TestOrder.objects.get(id=id)
    staff_order_detail.came_for_test = True
    staff_order_detail.save()

    return redirect('diagnostic_centers:staff-dashboard', username=username)

########################################################################################


def total_test_count_center_staff(request, id=None):

    order_count = TestOrder.objects.filter(test_info__center=id).count()

    template = 'tests/total_test_count/total_test_count_center_staff.html'

    context = {

        'order_count': order_count,
    }

    return render(request, template, context)

########################################################################################


