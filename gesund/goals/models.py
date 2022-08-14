from django.conf import settings
from django.db import models
from django.urls import reverse


class Goals(models.Model):
    """ Goals model. """
    id = models.AutoField(primary_key=True, editable=False)
    calories = models.FloatField(blank=True, default=0.0)
    pomodoro = models.FloatField(blank=True, default=0.0)
    steps = models.FloatField(blank=True, default=0.0)
    water = models.FloatField(blank=True, default=0.0)
    weight = models.FloatField(blank=True, default=0.0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.calories}, {self.steps}, {self.water} , {self.weight}'

    def get_absolute_url(self):
        return reverse('goals-index')
