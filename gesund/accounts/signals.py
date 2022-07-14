from django.conf import settings
from django.contrib.auth.models import User

from django.core.mail import EmailMultiAlternatives
#from django.core.mail import send_mail


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import get_template

from goals.models import Goals
from history.models import History
from profiles.models import Profile
from xps.models import XP


@receiver(post_save, sender=User)
def send_email(sender, instance, created, **kwargs):
    subject = 'Thank you for registering with Gesund App'
    from_email = settings.EMAIL_HOST_USER
    to = instance.email

    # text_content = 'This is an important message.'
    # html_content = '<p>This is an <strong>important</strong> message.</p>'

    d = {'username': instance.username}

    plaintext = get_template('send-email.txt')
    htmly = get_template('send-email.html')

    text_content = plaintext.render(d)
    html_content = htmly.render(d)

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

# @receiver(post_save, sender=User)
# def send_email(sender, instance, created, **kwargs):
#     """ Sends email after user is created. """
#     if created:
#         # send_mail('my subject',
#         #           'my message',
#         #           'sender@email.com',
#         #           ['receiver@email.com']
#         #           )
        
#         print('yoyoyo')
#         send_mail(
#             'Thank you for registering with Gesund App',
#             f'Dear {instance.username}, bla bla bla.',
#             settings.EMAIL_HOST_USER,
#             ['mhrj.asis@gmail.com']
#         )


@receiver(post_save, sender=User)
def history_account_create(sender, instance, created, **kwargs):
    """ Records history after account creation. """
    if created:
        _app = 'Account'
        _action = 'CREATE'
        _description = f'{instance} account created.'
        _author = instance
        History.objects.create(app=_app, action=_action, description=_description, author=_author)


@receiver(post_save, sender=User)
def create_account_xp(sender, instance, created, **kwargs):
    """ User earns 1000 XP when they sign up. """
    if created:
        XP.objects.create(xp=1000, author=instance)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """ Create profile after user instance creation. """
    if created:
        Profile.objects.create(author=instance)


@receiver(post_save, sender=User)
def create_goals(sender, instance, created, **kwargs):
    """ Create goals after user instance creation. """
    if created:
        Goals.objects.create(author=instance)
