# Generated by Django 2.2.4 on 2019-10-03 22:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0017_auto_20191004_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 3, 22, 1, 9, 229149, tzinfo=utc)),
        ),
    ]
