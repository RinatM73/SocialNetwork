# Generated by Django 4.1 on 2024-07-11 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='name_1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название фото'),
        ),
    ]