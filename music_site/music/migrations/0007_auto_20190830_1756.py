# Generated by Django 2.2.4 on 2019-08-30 14:56

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_auto_20190830_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='album',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='music.Album'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 30, 14, 56, 46, 407815, tzinfo=utc)),
        ),
    ]
