# Generated by Django 2.2.4 on 2020-01-07 11:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0011_friend'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeekDays',
            fields=[
                ('name', models.CharField(choices=[('MO', 'Monday'), ('TU', 'Tuesday'), ('WE', 'Wednesday'), ('TH', 'Thursday'), ('FR', 'Friday'), ('SA', 'Saturday'), ('SU', 'Sunday')], max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('start_event', models.DateTimeField(default=datetime.datetime(2020, 1, 7, 0, 0))),
                ('end_event', models.DateTimeField(default=datetime.datetime(2020, 1, 8, 0, 0))),
                ('notes', models.TextField(max_length=150)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
            ],
        ),
    ]
