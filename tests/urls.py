from django.urls import path

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
    delete_test,
    edit_test,

    confirm_payment_message,

    came_for_test,

)


app_name = 'tests'


urlpatterns = [

    path('all-tests/', all_tests, name='all-tests'),

    path('categories/', test_categories, name='categories'),

    path('categorise-tests/<int:id>/', categorise_tests, name='categorise-tests'),

    path('test-details/<int:id>/', test_details, name='test-details'),

    path('order/<int:id>/', test_order, name='order'),

    path('order-details/<int:id>/', order_details_info, name='order-details'),

    path('staff-approved/<int:id>/<username>/', staff_approved, name='staff-approved'),

    path('staff-rejected/<int:id>/<username>/', staff_rejected, name='staff-rejected'),

    path('add-test/<username>/', add_test_by_admin, name='add-test'),

    path('all-tests-list-staff-admin/', all_tests_list_for_staff_admin, name='all-tests-list-staff-admin'),

    path('delete-test/<int:id>/', delete_test, name='delete_test'),

    path('edit-test/<int:id>/', edit_test, name='edit-test'),

    path('confirm-payment-message/<int:id>/', confirm_payment_message, name='confirm-payment-message'),

    path('staff-confirm-payment-message/<int:id>/<username>/', confirm_payment_message, name='staff-confirm-payment-message'),

    path('came-for-test/<int:id>/<username>/', came_for_test, name='came-for-test'),


]


