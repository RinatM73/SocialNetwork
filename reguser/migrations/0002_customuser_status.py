# Generated by Django 4.1 on 2024-07-02 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reguser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='status',
            field=models.TextField(blank=True, max_length=400, null=True, verbose_name='Статус'),
        ),
    ]
