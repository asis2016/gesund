from django.contrib import admin
from .models import Steps


class StepsAdmin(admin.ModelAdmin):
    model = Steps
    list_display = ['id', 'datestamp', 'step_count', 'author']


admin.site.register(Steps, StepsAdmin)
