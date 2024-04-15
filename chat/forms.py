from django.forms import ModelForm
from chat.models import ChatMessage


class MessageForm(ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['message']
        labels = {'message': ""}