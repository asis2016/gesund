from django.contrib import admin
from .models import Weight


class WeightAdmin(admin.ModelAdmin):
    """ Admin for weight. """
    model = Weight
    list_display = ['id', 'datestamp', 'weight', 'author']


admin.site.register(Weight, WeightAdmin)
