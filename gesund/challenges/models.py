from datetime import datetime
from django.urls import reverse
from django.conf import settings
from django.db import models


class Challenge(models.Model):
    """Challenge model."""
    id = models.AutoField(primary_key=True, editable=False)
    start_date = models.DateTimeField()

    challenge_choices = [
        ('NO_ALCOHOL', 'No alcohol'),
        ('NO_CHOCOLATE', 'No chocolate'),
        ('NO_FAST_FOOD', 'No fast food'),
        ('NO_SMOKING', 'No smoking'),
        ('NO_SUGAR', 'No sugar')
    ]
    challenge = models.CharField(max_length=15, choices=challenge_choices)
    status = models.BooleanField(default=1)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.challenge} - {datetime.now()}'

    def get_duration(self):
        """ GET duration from start date."""
        val = datetime.now() - self.start_date
        return val

    def get_absolute_url(self):
        return reverse('challenges-index')
