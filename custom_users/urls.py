from django.urls import path

from .views import (

    profile,
    profile_edit,
    orders_by_user,
    filtered_report,

    # MyLoginView,
    # MySignupView,
    # MyPasswordResetView,
    # MyPasswordChangeView,
)


app_name = 'custom_users'

urlpatterns = [

    # path('login/', MyLoginView.as_view(), name='account_login'),

    path('profile/', profile, name='profile'),

    path('profile-edit/', profile_edit, name='profile-edit'),

    path('orders-by-user/', orders_by_user, name='orders-by-user'),

    path('filtered-reports-by-user/<int:id>/', filtered_report, name='filtered-reports-by-user')

    # path('password_reset', MyPasswordResetView.as_view(), name='account_reset_password'),

    # path('password/change/', MyPasswordChangeView, name='account_change_password'),


]


# from django.conf.urls import url
#
# from . import views
#
#
# urlpatterns = [
#     url(r"^signup/$", views.signup, name="account_signup"),

#     url(r"^login/$", views.login, name="account_login"),

#     url(r"^logout/$", views.logout, name="account_logout"),
#
#     url(r"^password/change/$", views.password_change, name="account_change_password"),

#     url(r"^password/set/$", views.password_set, name="account_set_password"),
#
#     url(r"^inactive/$", views.account_inactive, name="account_inactive"),
#
#     # E-mail:
#     url(r"^email/$", views.email, name="account_email"),

#     url(r"^confirm-email/$", views.email_verification_sent, name="account_email_verification_sent"),

#     url(r"^confirm-email/(?P<key>[-:\w]+)/$", views.confirm_email, name="account_confirm_email"),
#
#     # password reset:
#     url(r"^password/reset/$", views.password_reset, name="account_reset_password"),

#     url(r"^password/reset/done/$", views.password_reset_done, name="account_reset_password_done"),

#     url(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$", views.password_reset_from_key,
#         name="account_reset_password_from_key"),

#     url(r"^password/reset/key/done/$", views.password_reset_from_key_done,
#       name="account_reset_password_from_key_done"),
# ]
