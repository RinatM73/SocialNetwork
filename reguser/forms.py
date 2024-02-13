from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text="Выберите дату рождения",
    )
    class Meta:
        model = CustomUser
        fields = ['username', 'image_profile', 'email', 'first_name', 'last_name', 'birth_date',  'password1', 'password2']
