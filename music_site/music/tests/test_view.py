from django.test import (TestCase,
                         Client)
from django.urls import reverse
from music.views import (HomePage,
                         AlbumList,
                         TopAlbum,
                         SongAlbum,
                         CreateVote,
                         UpdateVote,
                         favourite,
                         favourite_list)
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from music.models import (Album,
                          Person,
                          SongsAlbum)
from django.core.files.uploadedfile import SimpleUploadedFile
import os


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = "test_view"
        self.password = "test_view12345678"
        self.user = User.objects.create_user(
            username=self.username,
            email="test_view@gmail.com",
            password=self.password,
        )
        self.user.save()
        self.person = Person.objects.create(
            first_name="name",
            last_name="surname",
            born=datetime(2010, 2, 12)
        )
        self.song_album_id = Album.objects.create(
            author_album="test123",
            name_album="test-test123",
            release_date=datetime.now(tz=timezone.utc),
            image_album=self.open_file().name,
            genre="test",
            author=self.person
        )

    def open_file(self):
        file_search = os.listdir(path="music/static/music/uploads")[10]
        file_open = SimpleUploadedFile(file_search, b"")
        return file_open

    def check_is_auth(self):
        return self.client.login(username=self.username, password=self.password)

    def test_view_home_page(self):
        url = reverse("music:home")
        if self.check_is_auth():
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

    def test_view_album_list(self):
        context = Album.objects.all()
        url = reverse("music:album-list")
        if self.check_is_auth():
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.context["contacts"]), len(context))

    def test_view_top_album(self):
        url = reverse("music:top_album")
        if self.check_is_auth():
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

    def test_view_song_album(self):
        url = reverse("music:SongAlbum", args=[self.song_album_id.id])
        if self.check_is_auth():
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)




