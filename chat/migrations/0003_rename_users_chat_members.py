# Generated by Django 4.1.13 on 2024-02-29 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_chat_create_date_alter_chatmessage_date_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='users',
            new_name='members',
        ),
    ]
