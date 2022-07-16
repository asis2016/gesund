from django.contrib import admin

from .models import Pomodoro


class PomodoroAdmin(admin.ModelAdmin):
    """ Admin for pomodoro. """
    model = Pomodoro
    list_display = ['id', 'datestamp', 'author']


admin.site.register(Pomodoro, PomodoroAdmin)
