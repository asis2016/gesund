from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from xps.models import XP


@receiver(post_save, sender=User)
def create_xps(sender, instance, created, **kwargs):
    """ User earns 1 XP when they sign up. """
    if created:
        XP.objects.create(xp=1, author=instance)
