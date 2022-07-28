from django.db import models

from .calorie_category import CalorieCategory


class CalorieFoodDetail(models.Model):
    """ Calories food detail model. """
    id = models.AutoField(primary_key=True, editable=False)
    food = models.TextField()
    description = models.TextField()
    calories = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    carb = models.FloatField()
    sugar = models.FloatField()
    fiber = models.FloatField()
    status = models.BooleanField()
    category = models.ForeignKey(CalorieCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.food} - {self.description}'
