from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    birth_date = models.DateField(verbose_name="Дата рождения", blank=True, null=True)
    age = models.PositiveIntegerField(verbose_name="Возраст", blank=True, null=True)
    image_profile = models.ImageField(upload_to='profile/image', verbose_name="Фото профиля", blank=True)
    country = models.CharField(max_length=250, verbose_name="Страна", blank=True, null=True)
    city = models.CharField(max_length=250, verbose_name="Город", blank=True, null=True)
    education = models.CharField(max_length=250, verbose_name="Образование", blank=True, null=True)
    job = models.CharField(max_length=250, verbose_name="Работа", blank=True, null=True)
    friends = models.ManyToManyField('CustomUser', blank=True)
    videos = models.FileField(verbose_name="Видео", upload_to='video/', blank=True, null=True)
    photos = models.ImageField(verbose_name="Фото", upload_to='photo/', blank=True, null=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'