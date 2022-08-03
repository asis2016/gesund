from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from history.models import History
from xps.models import XP

from .models import CalorieIntake


@receiver(post_save, sender=CalorieIntake)
def history_calories_create(sender, instance, created, **kwargs):
    """ Records history after creating calories. """
    if created:
        _app = 'Calories'
        _action = 'CREATE'
        _description = f'{instance.food} ({instance.calories} cal) intake.'
        _author = instance.author
        History.objects.create(app=_app, action=_action, description=_description, author=_author)


@receiver(post_save, sender=CalorieIntake)
def history_calories_update(sender, instance, created, **kwargs):
    """ Records history after updating calories. """
    if not created:
        _app = 'Calories'
        _action = 'UPDATE'
        _description = f'{instance.food} ({instance.calories} cal) intake updated.'
        _author = instance.author
        History.objects.create(app=_app, action=_action, description=_description, author=_author)


@receiver(post_delete, sender=CalorieIntake)
def history_calories_delete(sender, instance, **kwargs):
    """ Records history after deleting calories. """
    _app = 'Calories'
    _action = 'DELETE'
    _description = f'{instance.food} ({instance.calories} cal) deleted.'
    _author = instance.author
    History.objects.create(app=_app, action=_action, description=_description, author=_author)


@receiver(post_save, sender=CalorieIntake)
def create_calories_xp(sender, instance, created, **kwargs):
    """ Creates XP after creating calories instance. """
    if created:
        XP.objects.create(xp=1, author=instance.author, referer_app_id=f'calories_{instance.id}')


@receiver(post_delete, sender=CalorieIntake)
def delete_calories_xp(sender, instance, **kwargs):
    XP.objects.filter(referer_app_id=f'calories_{instance.id}').delete()
