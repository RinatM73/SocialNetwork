from django.contrib.auth.decorators import login_required
from django.urls import path
from chat import views as chat_views, views

urlpatterns = [
    path("chat/", chat_views.chatPage, name="chat-page"),
]