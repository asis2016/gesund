from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from history.models import History

from .models import Pomodoro


@receiver(post_save, sender=Pomodoro)
def history_pomodoro_create(sender, instance, created, **kwargs):
    """ Records history after creating pomodoro. """
    if created:
        _app = 'Pomodoro'
        _action = 'CREATE'
        _description = f'{instance.pomodoro} pomodoro added.'
        _author = instance.author
        History.objects.create(
            app=_app,
            action=_action,
            description=_description,
            author=_author
        )


@receiver(post_delete, sender=Pomodoro)
def history_pomodoro_delete(sender, instance, **kwargs):
    """ Records history after deleting pomodoro. """
    _app = 'Pomodoro'
    _action = 'DELETE'
    _description = f'{instance.pomodoro} pomodoro deleted.'
    _author = instance.author
    History.objects.create(app=_app, action=_action, description=_description, author=_author)
