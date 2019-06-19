from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.views.generic import (
    ListView,
    TemplateView,
    DetailView
)

from .models import DiagnosticCenter, DiagnosticAdmin, DiagnosticStaff
from .forms import AdminLoginForm, StaffLoginForm


class AllDiagnosticCenters(ListView):
    model = DiagnosticCenter
    template_name = 'diagnostic_centers/all_centers.html'


# class AdminDashboard(TemplateView):
#     template_name = 'diagnostic_centers/admin_dashboard.html'

def admin_dashboard(request, username=None):
    admin = DiagnosticAdmin.objects.get(username=username)
    return render(request, 'diagnostic_centers/admin_dashboard.html', {'admin': admin})


# class StaffDashboard(TemplateView):
#     template_name = 'diagnostic_centers/staff_dashboard.html'

# class StaffDashboard(ListView):
#
#     template_name = 'diagnostic_centers/staff_dashboard.html'
#
#     def get_queryset(self):
#         self.staff = get_object_or_404(DiagnosticStaff, name=self.kwargs['username'])
#         return self.staff
#
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = self.get_context_data(**kwargs)
#         # Add in the publisher
#         context['staff'] = self.staff
#         return context

def staff_dashboard(request, username):
    staff = DiagnosticStaff.objects.get(username=username)
    admins = DiagnosticAdmin.objects.filter(staff=staff)
    context = {
        'staff': staff,
        'admins': admins,
    }
    return render(request, 'diagnostic_centers/staff_dashboard.html', context)


def admin_login(request, template_name='diagnostic_centers/admin_login.html'):
    admin_login_form = AdminLoginForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            DiagnosticAdmin.objects.get(username=username, password=password)
            messages.success(request, 'Login Successful for {}'.format(username), extra_tags='html_safe')
            return redirect('diagnostic_centers:admin-dashboard', username)

        except DiagnosticAdmin.DoesNotExist:
            return redirect('diagnostic_centers:admin-login')

    context = {
        'admin_login_form': admin_login_form}

    return render(request, template_name, context)


def admin_logout(request):
    messages.success(request, 'Logged Out.', extra_tags='html_safe')
    return redirect('diagnostic_centers:admin-login')


def staff_login(request, template_name='diagnostic_centers/staff_login.html'):
    staff_login_form = StaffLoginForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            DiagnosticStaff.objects.get(username=username, password=password)
            messages.success(request, 'Login Successful for {}'.format(username), extra_tags='html_safe')
            return redirect('diagnostic_centers:staff-dashboard', username)

        except DiagnosticStaff.DoesNotExist:
            return redirect('diagnostic_centers:staff-login')

    context = {'staff_login_form': staff_login_form}

    return render(request, template_name, context)


def staff_logout(request):
    messages.success(request, 'Logged Out.', extra_tags='html_safe')
    return redirect('diagnostic_centers:staff-login')


