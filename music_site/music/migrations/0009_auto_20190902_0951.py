# Generated by Django 2.2.4 on 2019-09-02 06:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_auto_20190902_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='done',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 2, 6, 51, 2, 256902, tzinfo=utc)),
        ),
    ]
