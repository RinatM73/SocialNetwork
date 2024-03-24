from django.urls import path
from . import views

urlpatterns = [
    path('friends/', views.friends, name='friends'),
    path('add-friend/<int:id>', views.send_request, name='add-friend'),
    path('accept/<int:id>', views.accept_request, name='accept'),
    path('friends_det/<int:pk>', views.friends_det, name='friends_det'),
]