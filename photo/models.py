from django.db import models

from reguser.models import CustomUser


class Photo(models.Model):
    user_photo = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='photos')
    image_1 = models.ImageField('Фото', upload_to='photo/image/')
    name_1 = models.CharField(max_length=100, verbose_name='Название фото', blank=True)
    desc_1 = models.TextField(max_length=250, verbose_name='Описание')
    date_1 = models.DateField(verbose_name='Дата', auto_now_add=True)

    def __str__(self):
        return f"{self.desc_1} | {self.date_1}"

    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'Фото'
