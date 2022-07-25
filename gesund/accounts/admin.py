from django.contrib import admin

from .models import UserSignLog


class UserSignLogAdmin(admin.ModelAdmin):
    """ Admin for UserSignLog. """
    model = UserSignLog
    list_display = ['id', 'datestamp', 'log_status', 'author']


admin.site.register(UserSignLog, UserSignLogAdmin)
