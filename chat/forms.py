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

class NewGroupForm(ModelForm):
    class Meta:
        model = ChatGroup
        fields = ['groupchat_name']
        widgets = {
            'groupchat_name' : forms.TextInput(attrs={
                'placeholder': 'Введите название группы ...',
                'class': 'p-4 text-black',
                'maxlength' : '300',
                'autofocus': True,
                }),
        }

class ChatRoomEditForm(ModelForm):
    class Meta:
        model = ChatGroup
        fields = ['groupchat_name']
        widgets = {
            'groupchat_name' : forms.TextInput(attrs={
                'class': 'p-4 text-xl font-bold mb-4',
                'maxlength' : '300',
                }),
        }