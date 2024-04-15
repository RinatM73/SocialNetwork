from django.contrib import admin
from friends.models import FriendRequest


# Register your models here.
admin.register(FriendRequest)
class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user')