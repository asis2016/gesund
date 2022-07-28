from django.db import models


class CalorieCategory(models.Model):
    """ Calories category model. """
    id = models.AutoField(primary_key=True, editable=False)
    category = models.CharField(max_length=100)
    status = models.BooleanField()
