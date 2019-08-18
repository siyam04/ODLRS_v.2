from django.urls import path

from .views import all_reports, single_report_details, complete_due_payment


app_name = 'report_processing'

urlpatterns = [

    path('all-reports/', all_reports, name='all-reports'),

    path('single-report-details/<int:id>/', single_report_details, name='single-report-details'),

    path('complete-due-payment/<int:id>/<int:report_id>/', complete_due_payment, name='complete-due-payment'),

]



