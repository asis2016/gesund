from django.apps import AppConfig


class WeightsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weights'

    def ready(self):
        import weights.signals
