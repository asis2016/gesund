from django.contrib import admin
from .models import CalorieCategory, CalorieIntake, CalorieFoodDetail


class CalorieCategoryAdmin(admin.ModelAdmin):
    model = CalorieCategory
    list_display = ['id', 'category', 'status']


class CalorieIntakeAdmin(admin.ModelAdmin):
    model = CalorieIntake
    list_display = ['id', 'datestamp', 'food', 'consume', 'author']


class CalorieFoodAdmin(admin.ModelAdmin):
    model = CalorieFoodDetail
    list_display = ['id', 'food', 'calories', 'protein', 'carb', 'fat']


admin.site.register(CalorieCategory, CalorieCategoryAdmin)
admin.site.register(CalorieIntake, CalorieIntakeAdmin)
admin.site.register(CalorieFoodDetail, CalorieFoodAdmin)
