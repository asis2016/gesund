from django.conf import settings
from django.db import models


class History(models.Model):
    """ History model. """
    id = models.AutoField(primary_key=True, editable=False)
    datestamp = models.DateTimeField(auto_now_add=True)
    app = models.CharField(max_length=20)  # django app
    action = models.CharField(max_length=10)  # CRUD action
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'
