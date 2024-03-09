from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import *



urlpatterns = [
    path('register/', UserCreateView.as_view(), name = 'register'),
    path('login/', UserLogin.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile_update/<int:pk>', ProfileUpdateView.as_view(), name='profile_update'),
]