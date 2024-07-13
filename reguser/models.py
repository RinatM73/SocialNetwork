from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.
class CustomUser(AbstractUser):
    birth_date = models.DateField(verbose_name="Дата рождения", blank=True, null=True)
    age = models.PositiveIntegerField(verbose_name="Возраст", blank=True, null=True)
    image_profile = models.ImageField(upload_to='profile/image', verbose_name="Фото профиля", blank=True)
    country = models.CharField(max_length=250, verbose_name="Страна", blank=True)
    city = models.CharField(max_length=250, verbose_name="Город", blank=True)
    education = models.CharField(max_length=250, verbose_name="Образование", blank=True)
    job = models.CharField(max_length=250, verbose_name="Работа", blank=True)
    friends = models.ManyToManyField('CustomUser', blank=True)
    status = models.TextField(max_length=400, verbose_name="Статус", blank=True)
    phone_number = models.CharField(max_length=50, verbose_name="Номер телефона", blank=True)
    about_me = models.TextField(max_length=500, verbose_name="О себе", blank=True, null=True)
    facebook = models.URLField(max_length=150, verbose_name="Фэйсбук", blank=True)
    telegram = models.URLField(max_length=150, verbose_name="Телеграм", blank=True)
    instagram = models.URLField(max_length=150, verbose_name="Инстаграм", blank=True)

    def age(self):
        today = datetime.now().date()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age


    def __str__(self):
        return f'{self.first_name} {self.last_name}'