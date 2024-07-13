from django.urls import path
from . import views

urlpatterns = [
    path('photo/<int:id>', views.photo, name='photo'),
    path('photo/<int:pk>', views.photo_det, name='photo_det')
]