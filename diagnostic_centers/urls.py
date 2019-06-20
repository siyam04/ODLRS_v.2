from django.urls import path

from .views import (

    search_paginator,

    admin_login,
    admin_logout,
    AdminDashboard,

    staff_login,
    staff_logout,
    StaffDashboard,
)


app_name = 'diagnostic_centers'

urlpatterns = [

    # path('all-centers/', AllDiagnosticCenters.as_view(), name='all-centers'),
    path('all-centers/', search_paginator, name='all-centers'),
    path('admin-login/', admin_login, name='admin-login'),
    path('admin-logout/', admin_logout, name='admin-logout'),
    path('admin-dashboard/', AdminDashboard.as_view(), name='admin-dashboard'),

    path('staff-login/', staff_login, name='staff-login'),
    path('staff-logout/', staff_logout, name='staff-logout'),
    path('staff-dashboard/', StaffDashboard.as_view(), name='staff-dashboard'),

]
