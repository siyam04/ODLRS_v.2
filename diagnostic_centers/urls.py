from django.urls import path

from .views import (

    search_paginator,

    admin_login,
    admin_logout,
    admin_dashboard,

    staff_login,
    staff_logout,
    staff_dashboard,

    center_details,

)


app_name = 'diagnostic_centers'

urlpatterns = [

    path('all-centers/', search_paginator, name='all-centers'),

    path('admin-login/', admin_login, name='admin-login'),
    path('admin-logout/', admin_logout, name='admin-logout'),
    path('admin-dashboard/<username>/', admin_dashboard, name='admin-dashboard'),

    path('staff-login/', staff_login, name='staff-login'),
    path('staff-logout/', staff_logout, name='staff-logout'),
    path('staff-dashboard/<username>/', staff_dashboard, name='staff-dashboard'),
    path('staff-dashboard/<int:id>/<username>/', staff_dashboard, name='staff-dashboards'),

    path('center-details/<int:id>/', center_details, name='center-details'),


]
