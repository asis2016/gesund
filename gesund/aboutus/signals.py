from django.db.models.signals import post_save
from django.dispatch import receiver
from history.models import History

from .models import ContactUs


@receiver(post_save, sender=ContactUs)
def history_calories_create(sender, instance, created, **kwargs):
    """ Records history after creating calories. """
    if created:
        _app = 'Contact Admin'
        _action = 'MESSAGE SENT'
        _description = f'Subject: {instance.subject}'
        _author = instance.author
        History.objects.create(app=_app, action=_action, description=_description, author=_author)
