#
#
#   This django app is not completed.

from django.urls import reverse
from django.conf import settings
from django.db import models


class Pomodoro(models.Model):
    """Pomodoro model."""
    id = models.AutoField(primary_key=True, editable=False)
    datestamp = models.DateField(blank=True, null=True)
    pomodoro_minutes = models.FloatField(blank=True, null=True)
    break_minutes = models.FloatField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def calc_pomodoro(self):
        val = round(self.pomodoro_minutes / 25, 2)
        return val

    def get_absolute_url(self):
        return reverse('pomodoros-index')

    def __str__(self):
        return f'{self.author} - {self.pomodoro_minutes} taken.'
