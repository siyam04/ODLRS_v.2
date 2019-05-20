from django.urls import path

from .views import (
    profile,
    profile_update,
    MyLoginView,
    MySignupView,
)


app_name = 'custom_users'

urlpatterns = [

    path('login/', MyLoginView.as_view(), name='account_login'),

    path('signup/', MySignupView.as_view(), name='account_signup'),

    path('profile/', profile, name='profile'),

    path('profile-update/', profile_update, name='profile-update'),


]

