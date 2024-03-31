from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import register
from django.urls import reverse
from django.views import View

from chat.forms import MessageForm
from chat.models import Chat, ChatMessage


def chatPage(request, pk):
    chat = get_object_or_404(Chat, id=pk)
    chatmes = ChatMessage.objects.filter(chat=pk)
    if request.method == 'POST':
        formm = MessageForm(request.POST)
        if formm.is_valid():
            form = formm.save(commit=False)
            form.user = request.user
            form.chat = chat
            form.save()
            return redirect(chatPage, pk)
        else:
            form = MessageForm()
    return render(request, 'chatpage.html', {'chat': chat, 'chatmes': chatmes, 'form': form})



