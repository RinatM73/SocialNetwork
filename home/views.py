from django.shortcuts import render

from friends.models import FriendRequest
from reguser.models import CustomUser


def home(request):
    return render(request, 'home.html')