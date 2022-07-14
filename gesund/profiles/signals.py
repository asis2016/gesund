from django.db.models.signals import post_save
from django.dispatch import receiver
from history.models import History

from .models import Profile


@receiver(post_save, sender=Profile)
def history_profiles_update(sender, instance, **kwargs):
    """ Records history after updating profile. """
    _app = 'Profile'
    _action = 'UPDATE'
    _description = f'Profile updated.'
    _author = instance.author
    History.objects.create(app=_app, action=_action, description=_description, author=_author)
