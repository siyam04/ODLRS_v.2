from django.contrib import admin
from django.contrib.sites.models import Site

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    """Customizing Admin Interface"""
    list_display = ['id', 'user', 'profile_name', 'address', 'image']
    list_display_links = ['user']
    list_editable = ['profile_name']
    list_filter = ['user']
    search_fields = ['id', 'user', 'profile_name']


# Registering databases
admin.site.register(Profile, ProfileAdmin)


