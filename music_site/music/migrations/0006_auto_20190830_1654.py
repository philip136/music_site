# Generated by Django 2.2.4 on 2019-08-30 13:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0005_album_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='user',
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=100)),
                ('text', models.TextField(max_length=500)),
                ('publish_date', models.DateTimeField(default=datetime.datetime(2019, 8, 30, 13, 54, 34, 391981, tzinfo=utc))),
                ('like_comment', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]