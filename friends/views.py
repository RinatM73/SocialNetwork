from django.shortcuts import render, redirect, get_object_or_404

from friends.models import FriendRequest
from reguser.models import CustomUser


# Create your views here.
def friends(request):
    allusers = CustomUser.objects.exclude(username=request.user)
    fr = FriendRequest.objects.filter(to_user=request.user)
    return render(request, 'friends.html', {'allusers': allusers, 'fr': fr})
def send_request(request,id):
    from_user = request.user
    to_user = CustomUser.objects.get(id=id)
    frequest = FriendRequest.objects.get_or_create(from_user=from_user, to_user=to_user)
    return redirect('friends')

def accept_request(request,id):
    frequest = FriendRequest.objects.get(id=id)
    user1 = request.user
    user2 = frequest.from_user
    user1.friends.add(user2)
    user2.friends.add(user1)
    frequest = FriendRequest.objects.filter(id=id).delete()
    return redirect('friends')


def friends_det(request, pk):
    friend = get_object_or_404(CustomUser, id=pk)
    return render(request, 'friends_det.html', {'friend': friend})

def friends_mess():
    pass

