# Generated by Django 2.2.4 on 2020-01-31 21:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0070_auto_20200125_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 31, 21, 37, 11, 212384, tzinfo=utc)),
        ),
    ]
