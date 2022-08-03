from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from history.models import History
from xps.models import XP

from .models import Steps


@receiver(post_save, sender=Steps)
def history_steps_create(sender, instance, created, **kwargs):
    if created:
        """ Records history after creating steps. """
        _app = 'Steps'
        _action = 'CREATE'
        _description = f'{instance.step_count} steps added.'
        _author = instance.author
        History.objects.create(app=_app, action=_action, description=_description, author=_author)


# post_save.connect(create_steps, sender=Steps)

@receiver(post_save, sender=Steps)
def history_steps_update(sender, instance, created, **kwargs):
    if not created:
        """ Records history after updating steps. """
        _app = 'Steps'
        _action = 'UPDATE'
        _description = f'{instance.step_count} steps updated.'
        _author = instance.author
        History.objects.create(app=_app, action=_action, description=_description, author=_author)


@receiver(post_delete, sender=Steps)
def history_steps_delete(sender, instance, **kwargs):
    """ Records history after deleting steps. """
    _app = 'Steps'
    _action = 'DELETE'
    _description = f'{instance.step_count} steps deleted.'
    _author = instance.author
    History.objects.create(app=_app, action=_action, description=_description, author=_author)


@receiver(post_save, sender=Steps)
def create_steps_xp(sender, instance, created, **kwargs):
    """ Creates XP after creating steps instance. """
    if created:
        XP.objects.create(xp=1, author=instance.author, referer_app_id=f'steps_{instance.id}')


@receiver(post_delete, sender=Steps)
def delete_steps_xp(sender, instance, **kwargs):
    XP.objects.filter(referer_app_id=f'steps_{instance.id}').delete()
