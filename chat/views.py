from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from chat.forms import MessageForm
from chat.models import ChatMessage, Chat


def index(request):
  return render(request, 'chat/index.html')

# def room(request, chat_name):
#   author = request.GET.get('author', 'Anonymous')
#   messages = ChatMessage.objects.filter(chat=chat_name)[0:25]
#
#   return render(request, 'chat/room.html', {'chat_name': chat_name, 'author': author, 'messages': messages})

class DialogsView(View):
    def get(self, request):
        chats = Chat.objects.filter(members__in=[request.user.id])
        return render(request, 'chat/dialogs.html', {'user_profile': request.user, 'chats': chats})

class MessagesView(View):
    def get(self, request, chat_id):
        try:
            chat = Chat.objects.get(id=chat_id)
            if request.user in chat.members.all():
                chat.message_set.filter(is_readed=False).exclude(author=request.user).update(is_readed=True)
            else:
                chat = None
        except Chat.DoesNotExist:
            chat = None

        return render(
          request,
          'users/messages.html',
          {
            'user_profile': request.user,
            'chat': chat,
            'form': MessageForm()
          }
        )

    def post(self, request, chat_id):
        form = MessageForm(data=request.POST)
        if form.is_valid():
          message = form.save(commit=False)
          message.chat_id = chat_id
          message.author = request.user
          message.save()
        return redirect(reverse('users:messages', kwargs={'chat_id': chat_id}))

class CreateDialogView(View):
    def get(self, request, user_id):
        chats = Chat.objects.filter(members__in=[request.user.id, user_id])
        if chats.count() == 0:
            chat = Chat.objects.create()
            chat.members.add(request.user)
            chat.members.add(user_id)
        else:
            chat = chats.first()
        return redirect(reverse('users:messages', kwargs={'chat_id': chat.id}))