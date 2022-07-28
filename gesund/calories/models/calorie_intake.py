from django.conf import settings
from django.db import models
from django.urls import reverse

from .calorie_food_detail import CalorieFoodDetail


class CalorieIntake(models.Model):
    """ Calories intake model. """
    id = models.AutoField(primary_key=True, editable=False)
    datestamp = models.DateField(blank=True, null=True)
    food = models.TextField()
    consume = models.FloatField()
    description = models.TextField(blank=True, null=True)
    calories = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    carb = models.FloatField()
    sugar = models.FloatField()
    fiber = models.FloatField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    food_detail_ref = models.ForeignKey(CalorieFoodDetail, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.id}'

    def get_absolute_url(self):
        return reverse('calorie-intake-datestamp-index')
