from django.urls import path

<<<<<<< HEAD
from .views import all_tests, test_order, order_details_info, staff_approved, staff_rejected,payment_method,confirm_prement,reject_prement
=======
from .views import (

    all_tests,
    test_details,

    test_order,
    order_details_info,

    test_categories,
    categorise_tests,

    staff_approved,
    staff_rejected,

    add_test_by_admin,
    all_tests_list_for_staff_admin,

)
>>>>>>> master


app_name = 'tests'

urlpatterns = [

    path('all-tests/', all_tests, name='all-tests'),

    path('categories/', test_categories, name='categories'),

    path('categorise-tests/<int:id>/', categorise_tests, name='categorise-tests'),

    path('test-details/<int:id>/', test_details, name='test-details'),

    path('order/<int:id>/', test_order, name='order'),

    path('order-details/<int:id>/', order_details_info, name='order-details'),

    path('staff-approved/<int:id>/', staff_approved, name='staff-approved'),

    path('staff-rejected/<int:id>/', staff_rejected, name='staff-rejected'),

    path('add-test/', add_test_by_admin, name='add-test'),

<<<<<<< HEAD
    path('staff-rejected/<int:id>', staff_rejected, name='staff-rejected'),
    
    path('payment_method/<int:id>',payment_method,name="payment_method"),

    path('confirm_prement/<int:id>',confirm_prement,name="confirm_prement"),

    path('reject_prement/<int:id>',reject_prement,name="reject_prement")


=======
    path('all-tests-list-staff-admin/', all_tests_list_for_staff_admin, name='all-tests-list-staff-admin'),
>>>>>>> master

]
