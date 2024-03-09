from reguser.models import CustomUser
from djongo import models

# Create your models here.
class Chat(models.Model):
    chat_name = models.CharField(max_length=100, verbose_name='Название чата')
    members = models.ManyToManyField(CustomUser, verbose_name='Пользователь')
    create_date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)

class ChatMessage(models.Model):
    message = models.TextField(verbose_name='Текст сообщения')
    author = models.ForeignKey(CustomUser, verbose_name='Пользователь', on_delete=models.CASCADE)
    date_time = models.DateTimeField(verbose_name='Время собщения', auto_now_add=True)
    chat = models.ForeignKey(Chat, verbose_name='Чат', on_delete=models.CASCADE)

    class Meta:
        ordering = ['date_time']

    def __str__(self):
        return self.message