# Generated by Django 2.2.4 on 2019-08-16 20:45

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190816_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=sorl.thumbnail.fields.ImageField(default='default.png', upload_to='avatars'),
        ),
    ]
