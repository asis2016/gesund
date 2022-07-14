from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from history.models import History
from .models import Goals


@receiver(post_save, sender=Goals)
def history_goals_update(sender, instance, **kwargs):
    """ Records history after updating goals. """
    _app = 'Goals'
    _action = 'UPDATE'
    _description = f'Goals updated.'
    _author = instance.author
    History.objects.create(app=_app, action=_action, description=_description, author=_author)