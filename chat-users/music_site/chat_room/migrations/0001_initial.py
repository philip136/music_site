# Generated by Django 2.2.4 on 2019-10-04 01:51

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
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date create room')),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creater')),
                ('invited', models.ManyToManyField(related_name='invited_user', to=settings.AUTH_USER_MODEL, verbose_name='Party')),
            ],
            options={
                'verbose_name': 'Chat room',
                'verbose_name_plural': 'Chat rooms',
            },
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500, verbose_name='Message')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date message send')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat_room.Room', verbose_name='Chat room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Chat message',
                'verbose_name_plural': 'Chat messages',
            },
        ),
    ]
