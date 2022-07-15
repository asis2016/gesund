from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

from goals.models import Goals
from history.models import History
from profiles.models import Profile
from xps.models import XP


@receiver(post_save, sender=User)
def history_account_create(sender, instance, created, **kwargs):
    """ Records history after account creation. """
    if created:
        _app = 'Account'
        _action = 'CREATE'
        _description = f'{instance} account created.'
        _author = instance
        History.objects.create(app=_app, action=_action, description=_description, author=_author)


@receiver(post_save, sender=User)
def create_account_xp(sender, instance, created, **kwargs):
    """ User earns 1000 XP when they sign up. """
    if created:
        XP.objects.create(xp=1000, author=instance)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """ Create profile after user instance creation. """
    if created:
        Profile.objects.create(author=instance)


@receiver(post_save, sender=User)
def create_goals(sender, instance, created, **kwargs):
    """ Create goals after user instance creation. """
    if created:
        Goals.objects.create(author=instance)
