from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from goals.models import Goals


@receiver(post_save, sender=User)
def create_goals(sender, instance, created, **kwargs):
    """ Create goals after user instance creation. """
    if created:
        print(f'{instance} created. goals.')
        Goals.objects.create(author=instance)
