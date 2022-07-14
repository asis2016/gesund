from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import XP
from history.models import History


@receiver(post_save, sender=XP)
def history_xp_create(sender, instance, **kwargs):
    """ Records history after XP is automated. """
    _app = 'XP'
    _action = 'REWARDED'
    _description = f'{instance.xp} rewarded!'
    _author = instance.author
    History.objects.create(app=_app, action=_action, description=_description, author=_author)
