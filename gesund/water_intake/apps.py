from django.apps import AppConfig


class WaterIntakeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'water_intake'

    def ready(self):
        import water_intake.signals
