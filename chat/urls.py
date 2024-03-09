from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

# urlpatterns = [
#   path('index', views.index, name='index'),
#   path('chat/<str:chat_name>/', views.room, name='room'),
# ]

urlpatterns = [
  path('index', views.index, name='index'),
  path(r'^dialogs/$', login_required(views.DialogsView.as_view()), name='dialogs'),
  path(r'^dialogs/create/(?P<user_id>\d+)/$', login_required(views.CreateDialogView.as_view()), name='create_dialog'),
  path(r'^dialogs/(?P<chat_id>\d+)/$', login_required(views.MessagesView.as_view()), name='messages'),
]