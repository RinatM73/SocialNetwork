from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.views import LoginView

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text="Выберите дату рождения",
    )

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['image_profile'].widget.attrs.update({'class': 'form-control-file', 'accept': 'image/*'})
    class Meta:
        model = CustomUser
        fields = ['username', 'image_profile', 'email', 'first_name', 'last_name', 'birth_date',  'password1', 'password2']

class CustomUserChangeForm(UserChangeForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text="Выберите дату рождения",
    )
    class Meta:
        model = CustomUser
        fields = ['username', 'image_profile', 'email', 'first_name', 'last_name', 'birth_date']