from django.contrib import admin

from .models import OrderValidation


class OrderValidationAdmin(admin.ModelAdmin):
    list_display = ['id', 'approved_order_by_client', 'payment_status', 'confirmed_by_staff', 'confirmation_datetime']
    list_display_links = ['approved_order_by_client']
    # list_filter = ['approved_orders', 'confirmed_by_staff']
    search_fields = ['id', 'approved_order_by_client', 'confirmed_by_staff']
    list_editable = ['confirmed_by_staff']


# Registering databases
admin.site.register(OrderValidation, OrderValidationAdmin)

