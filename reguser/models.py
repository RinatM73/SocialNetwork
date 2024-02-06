from django.contrib.auth.models import User
from djongo import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250, verbose_name="Имя", blank=True, null=True)
    last_name = models.CharField(max_length=250, verbose_name="Фамилия", blank=True, null=True)
    birth_date = models.DateField(verbose_name="Дата рождения", blank=True, null=True)
    age = models.PositiveIntegerField(verbose_name="Возраст", blank=True, null=True)
    image_profile = models.ImageField(upload_to='profile/image')
    mail = models.EmailField(verbose_name="Почта", blank=True, null=True)
    country = models.CharField(max_length=250, verbose_name="Страна", blank=True, null=True)
    city = models.CharField(max_length=250, verbose_name="Город", blank=True, null=True)
    education = models.CharField(max_length=250, verbose_name="Образование", blank=True, null=True)
    job = models.CharField(max_length=250, verbose_name="Работа", blank=True, null=True)
    about_me = models.TextField(verbose_name="О себе", blank=True, null=True)
    phone_number = models.IntegerField(verbose_name="Телефон", blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()