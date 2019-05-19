
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from .views import Home, MyLoginView, MySignupView

urlpatterns = [


    # Super_user PATH
    path('admin/', admin.site.urls),

    # Home PATH
    path('', Home.as_view(), name='home'),

    # Accounts PATHs
    path('', include('custom_users.urls', namespace='custom_users')),

    # Built-in Auth PATHs
    path('accounts/', include('allauth.urls')),

    path('login/',MyLoginView.as_view(),name='account_login'),
    path('signup/',MySignupView.as_view(),name='account_signup'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


