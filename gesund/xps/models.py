from django.conf import settings
from django.db import models


class XP(models.Model):
    """ Experience Point (XP) model. """
    id = models.AutoField(primary_key=True, editable=False)
    xp = models.IntegerField(blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    datestamp = models.DateField(auto_now=True)
    referer_app_id = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.xp} - {self.author} - {self.datestamp}'
