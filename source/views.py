from django.views.generic import TemplateView
from diagnostic_centers.models import DiagnosticCenter
from django.views.generic import (
    ListView,
)

class HomeView(ListView):
    template_name = 'home.html'
    model = DiagnosticCenter
