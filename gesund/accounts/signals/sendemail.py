from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.core.mail import send_mail
from django.template.loader import get_template


@receiver(post_save, sender=User)
def send_email(sender, instance, created, **kwargs):
    """ Sends email after account is created. """
    subject = 'Thank you for registering with Gesund App'
    from_email = settings.EMAIL_HOST_USER
    to = instance.email

    try:
        d = {'username': instance.username}
        plaintext = get_template('accounts/send-email.txt')
        htmly = get_template('accounts/send-email.html')

        text_content = plaintext.render(d)  # 'This is an important message.'
        html_content = htmly.render(d)  # '<p>This is an <strong>important</strong> message.</p>'

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")

        msg.send()

    except Exception as e:
        raise e

#
#
#
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
