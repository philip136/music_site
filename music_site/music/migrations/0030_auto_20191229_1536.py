# Generated by Django 2.2.4 on 2019-12-29 12:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0029_auto_20191228_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 29, 12, 36, 26, 141267, tzinfo=utc)),
        ),
    ]
