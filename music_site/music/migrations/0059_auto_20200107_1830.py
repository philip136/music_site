# Generated by Django 2.2.4 on 2020-01-07 15:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0058_auto_20200107_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 7, 15, 30, 9, 416524, tzinfo=utc)),
        ),
    ]
