from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from accounts.models import UserSignLog

@receiver(user_logged_in)
def user_signs_in(sender, user, request, **kwargs):
    """ Posts when a user signs in. """
    UserSignLog.objects.create(log_status='signs in', author=user)


@receiver(user_logged_out)
def user_signs_out(sender, request, user, **kwargs):
    """ Posts when a user signs out. """
    UserSignLog.objects.create(log_status='signs out', author=user)
