from django.forms import ModelForm
from django import forms
from .models import *


class ChatMessageForm(ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['text']
        widgets = {
            'text': forms.TextInput(
                attrs={'placeholder': 'Введите сообщение ...', 'class': 'p-4 text-black',
                       'autofocus': True}),
        }