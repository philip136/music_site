# Generated by Django 2.2.4 on 2019-08-14 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_album', models.CharField(max_length=100)),
                ('name_album', models.CharField(max_length=140)),
                ('release_date', models.DateTimeField(null=True)),
                ('image_album', sorl.thumbnail.fields.ImageField(upload_to='uploads')),
                ('ratings', models.IntegerField(choices=[(0, 'NR - Not Rated'), (1, 'R - Rated')], default=0)),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=140)),
                ('last_name', models.CharField(max_length=140)),
                ('born', models.DateField()),
                ('died', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(choices=[(1, '+1'), (-1, '-1')])),
                ('voted_on', models.DateTimeField(auto_now=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Album')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SongsAlbum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_song', models.CharField(max_length=140)),
                ('file_song', models.FileField(upload_to='static/music/uploads/')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Album')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Person')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author', to='music.Person'),
        ),
    ]
