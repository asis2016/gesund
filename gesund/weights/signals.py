from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Weight
from history.models import History


@receiver(post_save, sender=Weight)
def history_weight_create(sender, instance, created, **kwargs):
    """ Records history after creating weight. """
    if created:
        _app = 'Weight'
        _action = 'CREATE'
        _description = f'{instance.weight} kg added.'
        _author = instance.author
        History.objects.create(app=_app, action=_action, description=_description, author=_author)


@receiver(post_save, sender=Weight)
def history_weight_update(sender, instance, created, **kwargs):
    """ Records history after updating weight. """
    if not created:
        _app = 'Weight'
        _action = 'UPDATE'
        _description = f'{instance.weight} kg updated.'
        _author = instance.author
        History.objects.create(app=_app, action=_action, description=_description, author=_author)


@receiver(post_delete, sender=Weight)
def history_weight_delete(sender, instance, **kwargs):
    """ Records history after deleting weight. """
    _app = 'Weight'
    _action = 'DELETE'
    _description = f'{instance.weight} kg deleted.'
    _author = instance.author
    History.objects.create(app=_app, action=_action, description=_description, author=_author)
