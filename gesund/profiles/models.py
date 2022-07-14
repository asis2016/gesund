from django.conf import settings
from django.db import models
from django.urls import reverse


class Profile(models.Model):
    """ Profile model. """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    CHOICES_GENDER = [
        ('F', 'F'),
        ('M', 'M'),
    ]
    gender = models.CharField(max_length=1, blank=True, null=True, choices=CHOICES_GENDER)
    height = models.FloatField(blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'Name: {self.id}, {self.author}'

    def get_absolute_url(self):
        return reverse('profile-index')
