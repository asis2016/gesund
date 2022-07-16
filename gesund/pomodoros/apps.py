from django.apps import AppConfig


class PomodorosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pomodoros'

    def ready(self):
        import pomodoros.signals
