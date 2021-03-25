from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'apps.users'
    verbose_name = 'Users'

    def ready(self):
        import apps.users.signals
