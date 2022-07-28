from django.conf import settings
from django.db import models
from django.urls import reverse


class WaterIntake(models.Model):
    """ Water intake model (daily) in liters. """
    id = models.AutoField(primary_key=True, editable=False)
    datestamp = models.DateField()
    drink_progress = models.FloatField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def get_average(self):
        """ Get average water intake. """
        avg_water_intake = sum(self.drink_progress)
        return avg_water_intake

    def get_absolute_url(self):
        return reverse('water-index')

    def __str__(self):
        return f'{self.datestamp} - {self.drink_progress} L.'
