# Generated by Django 2.2.4 on 2019-12-29 13:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0031_auto_20191229_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 29, 13, 8, 25, 614312, tzinfo=utc)),
        ),
    ]
