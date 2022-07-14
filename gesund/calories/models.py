from django.conf import settings
from django.urls import reverse
from django.db import models


class CalorieCategory(models.Model):
    """ Calories category model. """
    id = models.AutoField(primary_key=True, editable=False)
    category = models.CharField(max_length=100)
    status = models.BooleanField()


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


class CalorieIntake(models.Model):
    """ Calories intake model. """
    id = models.AutoField(primary_key=True, editable=False)
    datestamp = models.DateField(blank=True, null=True)
    food = models.TextField(blank=True, null=True)
    consume = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    calories = models.FloatField(blank=True, null=True)
    protein = models.FloatField(blank=True, null=True)
    fat = models.FloatField(blank=True, null=True)
    carb = models.FloatField(blank=True, null=True)
    sugar = models.FloatField(blank=True, null=True)
    fiber = models.FloatField(blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    food_detail_ref = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.id}'

    def get_absolute_url(self):
        return reverse('calorie-intake-datestamp-index')
