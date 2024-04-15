from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import register
from django.urls import reverse
from django.views import View

from chat.forms import MessageForm
from chat.models import Chat, ChatMessage


def chatPage(request):
    return render(request, 'chatpage.html')



