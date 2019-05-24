from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.views.generic import (
    ListView,
    DetailView,
)

from .models import DiagnosticCenter


class AllDiagnosticCenters(ListView):
    model = DiagnosticCenter
    template_name = 'diagnostic_centers/all_centers.html'
