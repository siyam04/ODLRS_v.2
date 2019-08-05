from django.contrib import admin

from .models import (

    TestCategory,
    Test,
    TestOrder,
)


class TestCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name', 'center']
    list_display_links = ['category_name']
    list_filter = ['category_name']
    search_fields = ['id', 'category_name']


class TestAdmin(admin.ModelAdmin):
    list_display = ['id', 'test_name', 'category', 'center', 'discount', 'price', 'active_status', 'image']
    list_display_links = ['test_name']
    list_filter = ['test_name', 'category']
    search_fields = ['id', 'test_name', 'center', 'category']


class TestOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'client_info', 'test_info', 'contact_no', 'email', 'address', 'payment_type', 'payment_method',
                    'booked_time_slot', 'booked_date', 'order_created_at', 'order_confirmed', 'staff_check', 'accepted',
                    'validation', 'came_for_test']

    list_editable = ['order_confirmed', 'came_for_test']

    list_display_links = ['client_info', 'test_info']
    # list_filter = ['client_info', 'test_info']
    search_fields = ['id', 'client_info', 'test_info', 'contact_no']


# Registering databases
admin.site.register(TestCategory, TestCategoryAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(TestOrder, TestOrderAdmin)


