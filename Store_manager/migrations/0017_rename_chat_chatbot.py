# Generated by Django 4.1.3 on 2022-12-06 08:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Store_manager', '0016_rename_chat_peopel2_chat__from_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='chat',
            new_name='chatbot',
        ),
    ]
