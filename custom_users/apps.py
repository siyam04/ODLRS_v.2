from django.apps import AppConfig


class CustomUsersConfig(AppConfig):
    name = 'custom_users'

    def ready(self):
        import custom_users.signals