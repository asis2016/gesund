from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class ContactUs(models.Model):
    """ Contact Us model. """
    id = models.AutoField(primary_key=True, editable=False)
    datestamp = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('about')
