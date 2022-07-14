from django.contrib import admin

from .models import Profile


class ProfileAdminRegister(admin.ModelAdmin):
    model = Profile
    list_display = ['id', 'dob', 'gender', 'height', 'author', ]


admin.site.register(Profile, ProfileAdminRegister)
