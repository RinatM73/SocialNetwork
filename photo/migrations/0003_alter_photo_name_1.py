# Generated by Django 4.1 on 2024-07-11 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_photo_name_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='name_1',
            field=models.CharField(blank=True, max_length=100, verbose_name='Название фото'),
        ),
    ]
