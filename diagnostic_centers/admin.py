from django.contrib import admin

from .models import (

    DiagnosticCenter,
    DiagnosticAdmin,
    DiagnosticStaff,
)

# 'Group' class hiding from the superuser

from django.contrib.auth.models import Group

admin.site.unregister(Group)


class DiagnosticCenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'contact_no', 'website', 'address', 'image']
    list_display_links = ['name']
    list_filter = ['name', 'email']
    search_fields = ['id', 'name', 'contact_no']


class DiagnosticAdminAdmin(admin.ModelAdmin):
    # list_display = ['id', 'username', 'password', 'center']
    list_display = ['id', 'username', 'center']
    list_display_links = ['username']
    list_filter = ['username', 'center']
    search_fields = ['id', 'username', 'center']
    filter_horizontal = ['staff']


class DiagnosticStaffAdmin(admin.ModelAdmin):
    # list_display = ['id', 'username', 'password', 'center']
    list_display = ['id', 'username', 'center']
    list_display_links = ['username']
    list_filter = ['username', 'center']
    search_fields = ['id', 'username', 'center']


# Registering databases
admin.site.register(DiagnosticCenter, DiagnosticCenterAdmin)
admin.site.register(DiagnosticAdmin, DiagnosticAdminAdmin)
admin.site.register(DiagnosticStaff, DiagnosticStaffAdmin)

#

