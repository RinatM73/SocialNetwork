from django.contrib import admin
from .models import Chat, ChatMessage
# Register your models here.
@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('chat_name', 'create_date')

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('author', 'date_time', 'chat')