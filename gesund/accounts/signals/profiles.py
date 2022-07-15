from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from profiles.models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """ Create profile after user instance creation. """
    if created:
        Profile.objects.create(author=instance)
