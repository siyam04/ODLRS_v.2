from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from custom_users.models import Profile

from .models import OrderValidation
from .forms import OrderValidationForm


########################################################################################


def order_validation_form(request, id=None):

    # this_client = Profile.objects.get(id=id)
    # this_order = OrderValidation.objects.get(id=id)

    if request.method == 'POST':
        final_order_validation_form = OrderValidationForm(request.POST)

        if final_order_validation_form.is_valid():
            final_order_validation_form.save()
            return redirect('reports:valid-order-details', id=id)

    else:
        final_order_validation_form = OrderValidationForm()

    template = 'reports/order_validation_form.html'
    context = {
        'final_order_validation_form': final_order_validation_form,
        # 'this_client': this_client,
        # 'this_order': this_order,
    }

    return render(request, template, context)

# def order_validation_form(request, id=None):
#
#     try:
#         current_profile = Profile.objects.get(user=request.user)
#         current_order = OrderValidation.objects.get(id=id)
#
#         # email = current_profile.user.email
#         # contact_no = current_profile.contact_no
#         # address = current_profile.address
#
#         initial_data = {
#             'current_profile': current_profile,
#             'current_order': current_order,
#             # 'email':email,
#             # 'contact_no': contact_no,
#             # 'address':address
#
#         }
#
#     except:
#         print('Test')
#         # return redirect('reports:order-validation-form', id=id)
#
#     if request.method == 'POST':
#         final_order_validation_form = OrderValidationForm(request.POST)
#
#         if final_order_validation_form.is_valid():
#             order = final_order_validation_form.save(commit=False)
#             order.save()
#             return redirect('reports:valid-order-details', id=order.id)
#
#     context = {
#         'final_order_validation_form': OrderValidationForm(initial=initial_data),
#     }
#
#     template = 'reports/order_validation_form.html'
#
#     return render(request, template, context)

########################################################################################


def valid_order_details(request, id=None):

    valid_order = get_object_or_404(OrderValidation, id=id)
    this_client = valid_order.approved_order_by_client.client_info.user.username
    this_test = valid_order.approved_order_by_client.test_info.test_name

    template = 'reports/valid_order_details.html'
    context = {
        'valid_order': valid_order,
        'this_client': this_client,
        'this_test': this_test,
    }

    return render(request, template, context)