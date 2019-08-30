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
    add_category_by_admin,
    filtered_categories_by_admin,
    filtered_categories_for_staff,

    delete_test,
    edit_test,

    edit_category,
    delete_category,

    all_tests_list_for_staff,
    added_tests_list_for_staff_admin,

    confirm_payment_message,

    came_for_test,

    total_test_count_center_staff,

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

    path('add-category/<username>/', add_category_by_admin, name='add-category'),

    path('filtered-categories-by-admin/<username>/', filtered_categories_by_admin, name='filtered-categories-by-admin'),

    path('filtered-categories-for-staff/<username>/', filtered_categories_for_staff, name='filtered-categories-for-staff'),

    path('all-tests-list-staff/<username>/', all_tests_list_for_staff, name='all-tests-list-staff'),

    path('added-tests-list-staff-admin/<username>/', added_tests_list_for_staff_admin, name='added-tests-list-staff-admin'),

    path('delete-test/<int:id>/<username>/', delete_test, name='delete_test'),

    path('delete-category/<int:id>/<username>/', delete_category, name='delete-category'),

    path('edit-test/<int:id>/<username>/', edit_test, name='edit-test'),

    path('edit-category/<int:id>/<username>/', edit_category, name='edit-category'),

    path('confirm-payment-message/<int:id>/', confirm_payment_message, name='confirm-payment-message'),

    path('staff-confirm-payment-message/<int:id>/<username>/', confirm_payment_message, name='staff-confirm-payment-message'),

    path('came-for-test/<int:id>/<username>/', came_for_test, name='came-for-test'),

    path('total-test-count-center-staff/<int:id>/', total_test_count_center_staff, name='total-test-count-center-staff'),


]


