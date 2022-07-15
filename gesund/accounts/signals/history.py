from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from history.models import History


@receiver(post_save, sender=User)
def create_history(sender, instance, created, **kwargs):
    """ Records history after account creation. """
    if created:
        _app = 'Account'
        _action = 'CREATE'
        _description = f'{instance} account created.'
        _author = instance
        History.objects.create(app=_app, action=_action, description=_description, author=_author)
