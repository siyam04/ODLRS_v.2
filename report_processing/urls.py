from django.urls import path

from .views import all_reports, single_report_details


app_name = 'report_processing'

urlpatterns = [

    path('all-reports/', all_reports, name='all-reports'),
    path('single-report-details/<int:id>/', single_report_details, name='single-report-details'),

]



