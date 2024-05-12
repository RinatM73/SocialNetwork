from reguser.models import CustomUser
from django.db import models
import shortuuid
from django.conf import settings
import os


# Create your models here.

class ChatGroup(models.Model):
    group_name = models.CharField(max_length=128, verbose_name="Имя группы", unique=True, default=shortuuid.uuid)
    users_online = models.ManyToManyField(CustomUser, related_name='online_in_groups', blank=True)
    members = models.ManyToManyField(CustomUser, related_name='chat_groups', blank=True)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.group_name

class ChatMessage(models.Model):
    group = models.ForeignKey(ChatGroup, verbose_name="Группа", related_name='chat_messages', on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, verbose_name='Отправитель', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст сообщения')
    created = models.DateTimeField(verbose_name='Время сообщения', auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} : {self.text}'
    class Meta:
        ordering = ['-created']