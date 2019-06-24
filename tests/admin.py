from django.contrib import admin

from .models import (

    TestCategory,
    Test,
    TestOrder,
)


class TestCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name']
    list_filter = ['category_name']
    search_fields = ['id', 'category_name']


class TestAdmin(admin.ModelAdmin):
    list_display = ['id', 'test_name', 'category', 'center', 'discount', 'price', 'active_status', 'image']
    list_display_links = ['test_name']
    list_filter = ['test_name', 'category']
    search_fields = ['id', 'test_name', 'center', 'category']


class TestOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'client_info', 'test_info', 'contact_no', 'payment_option', 'date', 'time', 'staff_check']
    list_display_links = ['client_info', 'test_info']
    list_filter = ['client_info', 'test_info']
    search_fields = ['id', 'client_info', 'test_info']


# Registering databases
admin.site.register(TestCategory, TestCategoryAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(TestOrder, TestOrderAdmin)