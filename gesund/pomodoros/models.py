from django.conf import settings
from django.db import models
from django.urls import reverse


class Pomodoro(models.Model):
    """Pomodoro model."""
    id = models.AutoField(primary_key=True, editable=False)
    datestamp = models.DateField(blank=True, null=True)
    pomodoro = models.IntegerField(blank=True, null=True)
    short_break = models.IntegerField(blank=True, null=True)
    long_break = models.IntegerField(blank=True, null=True)

    remarks = models.TextField(blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('pomodoro-index')
