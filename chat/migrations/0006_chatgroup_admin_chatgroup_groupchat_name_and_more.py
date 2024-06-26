# Generated by Django 4.1 on 2024-05-19 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.main


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0005_alter_chatgroup_group_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatgroup',
            name='admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='groupchats', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chatgroup',
            name='groupchat_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='chatgroup',
            name='group_name',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=128, unique=True, verbose_name='Имя группы'),
        ),
    ]
