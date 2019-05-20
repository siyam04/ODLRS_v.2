
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from .views import HomeView


urlpatterns = [


    # Super_user PATH
    path('admin/', admin.site.urls),

    # Home PATH
    path('', HomeView.as_view(), name='home'),

    # Accounts PATH
    path('', include('custom_users.urls', namespace='custom_users')),

    # Allauth PATH
    path('accounts/', include('allauth.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


