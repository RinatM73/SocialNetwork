# Generated by Django 4.1.13 on 2024-02-04 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=250, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=250, null=True, verbose_name='Фамилия')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('age', models.PositiveIntegerField(blank=True, null=True, verbose_name='Возраст')),
                ('image_profile', models.ImageField(upload_to='profile/image')),
                ('mail', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта')),
                ('country', models.CharField(blank=True, max_length=250, null=True, verbose_name='Страна')),
                ('city', models.CharField(blank=True, max_length=250, null=True, verbose_name='Город')),
                ('education', models.CharField(blank=True, max_length=250, null=True, verbose_name='Образование')),
                ('job', models.CharField(blank=True, max_length=250, null=True, verbose_name='Работа')),
                ('about_me', models.TextField(blank=True, null=True, verbose_name='О себе')),
                ('phone_number', models.IntegerField(blank=True, null=True, verbose_name='Телефон')),
            ],
        ),
    ]
