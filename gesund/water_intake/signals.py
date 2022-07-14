from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import WaterIntake
from xps.models import XP
from history.models import History


@receiver(post_save, sender=WaterIntake)
def history_water_intake_create(sender, instance, created, **kwargs):
    """ Records history after creating water intake. """
    if created:
        _app = 'Water intake'
        _action = 'CREATE'
        _description = f'{instance.drink_progress} liters water intake.'
        _author = instance.author
        History.objects.create(app=_app, action=_action, description=_description, author=_author)


@receiver(post_save, sender=WaterIntake)
def history_water_intake_update(sender, instance, created, **kwargs):
    """ Records history after updating water intake. """
    if not created:
        _app = 'Water intake'
        _action = 'UPDATE'
        _description = f'{instance.drink_progress} liters water intake updated.'
        _author = instance.author
        History.objects.create(app=_app, action=_action, description=_description, author=_author)


@receiver(post_delete, sender=WaterIntake)
def history_water_intake_delete(sender, instance, **kwargs):
    """Records history after deleting water intake. """
    _app = 'Water intake'
    _action = 'DELETE'
    _description = f'{instance.drink_progress} liters water intake deleted.'
    _author = instance.author
    History.objects.create(app=_app, action=_action, description=_description, author=_author)


@receiver(post_save, sender=WaterIntake)
def create_water_intake(sender, instance, created, **kwargs):
    """ Creates XP after creating water_intake instance. """
    if created:
        ml = int(instance.drink_progress * 1000)
        XP.objects.create(xp=ml, author=instance.author)
