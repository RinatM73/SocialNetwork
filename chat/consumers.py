import json

from channels.generic.websocket import AsyncWebsocketConsumer # The class we're using
from asgiref.sync import sync_to_async # Implement later

from chat.models import ChatMessage


class ChatConsumer(AsyncWebsocketConsumer):
  async def connect(self):
    self.chat_name = self.scope['url_route']['kwargs']['chat_name']
    self.chat_group_name = 'chat_%s' % self.chat_name

    # Join room group
    await self.channel_layer.group_add(
      self.chat_group_name,
      self.channel_name
    )

    await self.accept()

  async def disconnect(self, close_code):
    # Leave room group
    await self.channel_layer.group_discard(
      self.chat_group_name,
      self.channel_name
  )

  # Receive message from WebSocket
  async def receive(self, text_data):
    data = json.loads(text_data)
    message = data['message']
    author = data['author']
    chat = data['chat']

    await self.save_message(self, author, chat, message)

    # Send message to room group
    await self.channel_layer.group_send(
      self.chat_group_name,
      {
        'type': 'chat_message',
        'message': message,
        'author': author
      }
    )

  # Receive message from room group
  async def chat_message(self, event):
    message = event['message']
    author = event['author']

    # Send message to WebSocket
    await self.send(text_data=json.dumps({
      'message': message,
      'author': author
    }))


  @sync_to_async
  def save_message(self, author, chat, message):
    ChatMessage.object.create(username=author, chat=chat, text=message)