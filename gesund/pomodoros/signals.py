from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from history.models import History
from xps.models import XP

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


@receiver(post_save, sender=Pomodoro)
def create_pomodoro_xp(sender, instance, created, **kwargs):
    """ Creates XP after creating pomodoro instance. """
    if created:
        XP.objects.create(xp=1, author=instance.author, referer_app_id=f'pomodoro_{instance.id}')


@receiver(post_delete, sender=Pomodoro)
def delete_pomodoro_xp(sender, instance, **kwargs):
    XP.objects.filter(referer_app_id=f'pomodoro_{instance.id}').delete()
