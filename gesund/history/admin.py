from django.contrib import admin
from .models import History


class HistoryAdminRegister(admin.ModelAdmin):
    model = History
    list_display = ['id', 'author', 'datestamp', 'app', 'action', 'description', ]


admin.site.register(History, HistoryAdminRegister)
