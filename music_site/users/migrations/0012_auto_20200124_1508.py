# Generated by Django 2.2.4 on 2020-01-24 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_friend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='current_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='users.Profile'),
        ),
        migrations.AlterField(
            model_name='friend',
            name='users',
            field=models.ManyToManyField(to='users.Profile'),
        ),
    ]
