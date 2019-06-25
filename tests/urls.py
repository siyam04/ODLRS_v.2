from django.urls import path

from .views import all_tests, test_order, order_details_info, staff_approved, staff_rejected,payment_method,confirm_prement,reject_prement


app_name = 'tests'

urlpatterns = [

    path('all-tests/', all_tests, name='all-tests'),

    path('order/<int:id>', test_order, name='order'),

    path('order-details/<int:id>', order_details_info, name='order-details'),

    path('staff-approved/<int:id>', staff_approved, name='staff-approved'),

    path('staff-rejected/<int:id>', staff_rejected, name='staff-rejected'),
    
    path('payment_method/<int:id>',payment_method,name="payment_method"),

    path('confirm_prement/<int:id>',confirm_prement,name="confirm_prement"),

    path('reject_prement/<int:id>',reject_prement,name="reject_prement")



]
