from django.conf import settings
from django.db import models


class UserSignLog(models.Model):
    """ UserSignLog model. """
    id = models.AutoField(primary_key=True, editable=False)
    datestamp = models.DateTimeField(auto_now=True)
    log_status = models.CharField(max_length=10)  # signs in or signs out
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
