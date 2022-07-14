from django.contrib import admin
from .models import WaterIntake


class WaterAdminRegister(admin.ModelAdmin):
    model = WaterIntake
    list_display = ['id', 'datestamp', 'drink_progress', 'author']


admin.site.register(WaterIntake, WaterAdminRegister)
