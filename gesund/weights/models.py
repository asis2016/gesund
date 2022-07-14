from django.urls import reverse
from django.db import models


class Weight(models.Model):
    """ Weight model (measured in kg). """
    id = models.AutoField(primary_key=True, editable=False)
    datestamp = models.DateField()
    weight = models.FloatField()
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.datestamp} - {self.weight} kg'

    def get_absolute_url(self):
        return reverse('weight-index')
