from django.urls import path
from . import consumers

# Here, "" is routing to the URL ChatConsumer which
# will handle the chat functionality.
websocket_urlpatterns = [
	path('ws/chatroom/<chatroom_name>', consumers.ChatConsumer.as_asgi()),
]
