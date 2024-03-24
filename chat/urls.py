from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
  path('index/', views.index, name='index'),
  path('index/<str:room_name>/', views.room, name='room'),

]