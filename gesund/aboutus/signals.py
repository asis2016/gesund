from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from history.models import History

from .models import ContactUs


@receiver(post_save, sender=ContactUs)
def history_contactus_create(sender, instance, created, **kwargs):
    """ Records history after creating contact us. """
    if created:
        _app = 'Contact Admin'
        _action = 'CREATE'
        _description = f'Subject ({instance.subject}) was sent.'
        _author = instance.author
        History.objects.create(app=_app, action=_action, description=_description, author=_author)


@receiver(post_save, sender=ContactUs)
def send_email(sender, instance, created, **kwargs):
    """ Sends email after ContactUs instance created. """
    if created:
        author_email = instance.author.email
        _from = settings.NOREPLY_EMAIL
        _to = settings.RECEIVE_EMAIL_AT
        _date = instance.datestamp
        email_subject = 'You have received an email'
        contact_subject = instance.subject
        contact_message = instance.message

        text_content = 'This is an important message.'
        html_content = f'<p>Hi there,</p><p>Email from: {author_email}</p><p>Datetime: {_date}</p><p>Subject: {contact_subject}</p><p>Message: {contact_message}</p>'

        msg = EmailMultiAlternatives(email_subject, text_content, _from, [_to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
