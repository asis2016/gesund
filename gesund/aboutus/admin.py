from django.contrib import admin

from .models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):
    model = ContactUs
    list_display = ['id', 'datestamp', 'subject']


admin.site.register(ContactUs, ContactUsAdmin)
