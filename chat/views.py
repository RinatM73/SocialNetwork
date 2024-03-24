from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from chat.forms import MessageForm
from chat.models import ChatMessage, Chat


def index(request):
  return render(request, 'chat/index.html')

def room(request, room_name):
  username = request.GET.get('username', 'Anonymous')
  messages = ChatMessage.objects.filter(chat=room_name)[0:25]

  return render(request, 'chat/room.html', {'room_name': room_name, 'username': username, 'messages': messages})
