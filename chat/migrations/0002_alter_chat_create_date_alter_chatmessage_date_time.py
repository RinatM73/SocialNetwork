# Generated by Django 4.1.13 on 2024-02-27 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время собщения'),
        ),
    ]
