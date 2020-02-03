from django.test import TestCase
from django.urls import (reverse,
                         resolve)
from music.views import (HomePage,
                         AlbumList,
                         TopAlbum,
                         SongAlbum,
                         CreateVote,
                         UpdateVote,
                         favourite,
                         favourite_list)
from music.models import (Album,
                          Person,
                          SongsAlbum,
                          Comments)
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
import os


class TestUrls(TestCase):
    @property
    def generate_file(self):
        file_search = os.listdir(path="music/static/music/uploads")[10]
        file_open = SimpleUploadedFile(file_search, b"")
        return file_open

    def setUp(self):
        self.user = User.objects.create_user(
            username="test_urls",
            email="test_urls@gmail.com",
            password="test_urls12345678"
        )
        self.user.save()
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

    def test_home_url_is_resolved(self):
        url = reverse("music:home")
        self.assertEqual(resolve(url).func.view_class, HomePage)

    def test_album_list_url_is_resolved(self):
        url = reverse("music:album-list")
        self.assertEqual(resolve(url).func.view_class, AlbumList)

    def test_top_album_url_is_resolved(self):
        url = reverse("music:top_album")
        self.assertEqual(resolve(url).func.view_class, TopAlbum)

    def test_songs_album_url_is_resolved(self):
        song_album_id = self.songs_album.id
        url = reverse("music:SongAlbum", args=[song_album_id])
        self.assertEqual(resolve(url).func.view_class, SongAlbum)

    def test_create_vote_url_is_resolved(self):
        album_id = self.album.id
        url = reverse("music:CreateVote", args=[album_id])
        self.assertEqual(resolve(url).func.view_class, CreateVote)

    def test_favourite_song_url_is_resolved(self):
        song_id = self.songs_album.id
        url = reverse("music:favourite", args=[song_id])
        self.assertEqual(resolve(url).func, favourite)

    def test_favourite_list_url_is_resolved(self):
        url = reverse("music:favourite_list")
        self.assertEqual(resolve(url).func, favourite_list)



