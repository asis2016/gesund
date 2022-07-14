from django.conf import settings
from django.urls import reverse
from django.db import models


class Steps(models.Model):
    """ Steps model. """
    id = models.AutoField(primary_key=True, editable=False)
    datestamp = models.DateField()
    step_count = models.IntegerField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.datestamp} - {self.step_count}'

    def get_absolute_url(self):
        return reverse('steps-index')
