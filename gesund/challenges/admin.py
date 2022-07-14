from django.contrib import admin
from .models import Challenge


class ChallengesAdmin(admin.ModelAdmin):
    """Admin for Challenge."""
    model = Challenge
    list_display = ['id', 'status', 'challenge', 'start_date',  'author']


admin.site.register(Challenge, ChallengesAdmin)
