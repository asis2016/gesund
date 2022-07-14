from django.contrib import admin
from .models import Goals


class GoalsAdmin(admin.ModelAdmin):
    model = Goals
    list_display = ['id', 'calories', 'steps', 'water','weight', 'author']


admin.site.register(Goals, GoalsAdmin)
