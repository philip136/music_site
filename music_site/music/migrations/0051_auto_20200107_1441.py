# Generated by Django 2.2.4 on 2020-01-07 11:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0050_auto_20200107_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 7, 11, 41, 48, 901654, tzinfo=utc)),
        ),
    ]
