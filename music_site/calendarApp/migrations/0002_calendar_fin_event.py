# Generated by Django 2.2.4 on 2020-01-29 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar',
            name='fin_event',
            field=models.BooleanField(default=False),
        ),
    ]
