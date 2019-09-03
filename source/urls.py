
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from .views import home
from .views import DevelopersView


urlpatterns = [


    # Superuser
    path('admin/', admin.site.urls),

    # Home
    path('', home, name='home'),

    # App1 (custom_users)
    path('', include('custom_users.urls', namespace='custom_users')),

    # App2 (diagnostic_centers)
    path('', include('diagnostic_centers.urls', namespace='diagnostic_centers')),

    # App3 (tests)
    path('', include('tests.urls', namespace='tests')),

    # App3 (report_processing)
    path('', include('report_processing.urls', namespace='report_processing')),

    # Allauth (built-in)
    path('accounts/', include('allauth.urls')),

    # Developers
    path('developers/', DevelopersView.as_view(), name='developers'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


