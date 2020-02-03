from django.test import TestCase
from music.models import (Album,
                          Person,
                          SongsAlbum,
                          Comments)
from datetime import datetime
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
import os


class TestModels(TestCase):
    @property
    def generate_file(self):
        file_search = os.listdir(path="music/static/music/uploads")[10]
        file_open = SimpleUploadedFile(file_search, b"")
        return file_open

    @property
    def create_user(self):
        u = User.objects.create_user(
            username="test_music",
            email="test_music@gmail.com",
            password="test12345678"
        )
        u.save()
        return u

    def setUp(self):
        self.user = self.create_user
        self.author = Person.objects.create(
            first_name="test-test",
            last_name="testovich",
            born=datetime(1994, 2, 20)
        )
        self.author.save()
        self.album = Album.objects.create(
            author_album="test",
            name_album="test",
            release_date=datetime.now(tz=timezone.utc),
            genre="test",
            author=self.author
        )
        self.album.save()
        self.songs_album = SongsAlbum.objects.create(
            person=self.author,
            album=self.album,
            name_song=self.generate_file.name,
            file_song=self.generate_file
        )
        self.songs_album.save()
        self.comments = Comments.objects.create(
            album=self.album,
            post="test",
            author=self.user,
            text="comment text",
        )
        self.comments.save()

    def test_views_query_album(self):
        self.assertEqual(self.album.name_album, self.album.__str__())

    def test_views_query_songs_album(self):
        str_song = (self.songs_album.album.name_album + "_-_" + self.songs_album.name_song)
        self.assertEqual(str_song, self.songs_album.__str__())

    def test_views_query_comments(self):
        self.assertEqual(self.comments.text, self.comments.__str__())
