from django.shortcuts import render, get_object_or_404, redirect

from custom_users.models import Profile

from .models import Test, TestCategory, TestOrder
from .forms import TestOrderForm

from django.contrib.auth.models import User


def all_tests(request, template_name='tests/all_tests.html'):
    all_test_list = Test.objects.all()

    context = {'all_test_list': all_test_list}

    return render(request, template_name, context)


def test_order(request, id=id):

    try:
        current_profile = Profile.objects.get(user=request.user)
        current_test = Test.objects.get(id=id)

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


def order_details_info(request, id=None):
    order_details = TestOrder.objects.get(id=id)

    template = 'tests/order_details.html'

    context = {
        'order_details': order_details,
    }

    return render(request, template, context)


def payment_method(request,template="tests/paynent_method.html",id=None):

    order_details = TestOrder.objects.get(id=id)

    context = {
        'order_details': order_details,
    }

    return render(request,template,context)


def confirm_prement(request, id = None):

    messages.success(request, "Payment Successfull")
    order_details = TestOrder.objects.get(id=id)

    return redirect("tests:order-details", id=order_details.id)

def reject_prement(request, id = None):
    
    messages.error(request, "Order Reject")
    order_details = TestOrder.objects.get(id=id)

    return redirect("tests:order-details", id=order_details.id)


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


