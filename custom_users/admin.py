from django.contrib import admin
from django.contrib.sites.models import Site

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    """Customizing Admin Interface"""
    list_display = ['id', 'user', 'image']
    list_display_links = ['user']
    list_filter = ['user']
    search_fields = ['id', 'user']


# Registering databases
admin.site.register(Profile, ProfileAdmin)


