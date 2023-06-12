# Generated by Django 3.2.18 on 2023-06-12 01:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserChatRooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_presenter', models.PositiveSmallIntegerField(default=0)),
                ('chatroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.chatrooms')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='chatrooms',
            name='user_chat_rooms',
            field=models.ManyToManyField(related_name='chat_rooms', through='chat.UserChatRooms', to=settings.AUTH_USER_MODEL),
        ),
    ]