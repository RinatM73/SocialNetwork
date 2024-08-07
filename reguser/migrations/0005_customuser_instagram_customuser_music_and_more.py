# Generated by Django 4.1 on 2024-07-08 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reguser', '0004_customuser_about_me'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='instagram',
            field=models.URLField(blank=True, max_length=150, null=True, verbose_name='Инстаграм'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='music',
            field=models.FileField(blank=True, null=True, upload_to='music/', verbose_name='Музыка'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='telegram',
            field=models.URLField(blank=True, max_length=150, null=True, verbose_name='Телеграм'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='vk',
            field=models.URLField(blank=True, max_length=150, null=True, verbose_name='ВК'),
        ),
    ]
