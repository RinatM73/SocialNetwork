from django.urls import path

from friends.views import send_request, accept_request, friends

urlpatterns = [
    path('friends/', friends, name='friends'),
    path('add-friend/<int:id>', send_request, name='add-friend'),
    path('accept/<int:id>', accept_request, name='accept'),
]