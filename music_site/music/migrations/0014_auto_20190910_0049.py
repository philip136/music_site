# Generated by Django 2.2.4 on 2019-09-09 21:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0013_auto_20190908_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='data',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 9, 21, 48, 56, 512079, tzinfo=utc)),
        ),
    ]