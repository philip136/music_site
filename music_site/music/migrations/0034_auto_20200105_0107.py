# Generated by Django 2.2.4 on 2020-01-04 22:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0033_auto_20200105_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 4, 22, 7, 24, 317963, tzinfo=utc)),
        ),
    ]