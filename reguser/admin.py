from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')