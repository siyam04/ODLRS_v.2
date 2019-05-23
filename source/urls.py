
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

    # Allauth (built-in)
    path('accounts/', include('allauth.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


