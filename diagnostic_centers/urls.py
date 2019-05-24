from django.urls import path

from .views import (
    AllDiagnosticCenters,
)


app_name = 'diagnostic_centers'

urlpatterns = [

    path('all-centers/', AllDiagnosticCenters.as_view(), name='all-centers'),

]
