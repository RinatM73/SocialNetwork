# Generated by Django 4.1 on 2024-07-11 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_1', models.ImageField(upload_to='photo/image/', verbose_name='Фото')),
                ('desc_1', models.TextField(max_length=250, verbose_name='Описание')),
                ('date_1', models.DateField(auto_now_add=True, verbose_name='Дата')),
                ('user_photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'фото',
                'verbose_name_plural': 'Фото',
            },
        ),
    ]