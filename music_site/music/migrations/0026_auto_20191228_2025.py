# Generated by Django 2.2.4 on 2019-12-28 17:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0025_auto_20191005_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 28, 17, 25, 17, 537752, tzinfo=utc)),
        ),
    ]
