from django.urls import path

from .views import (

    order_validation_form,
    valid_order_details,

)


app_name = 'reports'


urlpatterns = [

    path('order-validation-form/<int:id>/', order_validation_form, name='order-validation-form'),

    path('valid-order-details/<int:id>/', valid_order_details, name='valid-order-details'),

    # path('categorise-tests/<int:id>/', categorise_tests, name='categorise-tests'),

]


