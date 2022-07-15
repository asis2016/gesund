from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        from .signals import goals
        from .signals import history
        from .signals import profiles
        from .signals import xps
        from .signals import sendemail
