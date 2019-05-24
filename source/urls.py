
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from .views import HomeView


urlpatterns = [


    # Superuser
    path('admin/', admin.site.urls),

    # Home
    path('', HomeView.as_view(), name='home'),

    # App1 (custom_users)
    path('', include('custom_users.urls', namespace='custom_users')),

    # App2 (diagnostic_centers)
    path('', include('diagnostic_centers.urls', namespace='diagnostic_centers')),

    # Allauth (built-in)
    path('accounts/', include('allauth.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


