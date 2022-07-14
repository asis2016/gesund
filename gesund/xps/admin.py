from django.contrib import admin
from .models import XP


class XPAdmin(admin.ModelAdmin):
    model = XP
    list_display = ['id', 'datestamp', 'author', 'xp']


admin.site.register(XP, XPAdmin)
