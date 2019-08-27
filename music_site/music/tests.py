from django.test import TestCase
from django.urls import (reverse,
                         resolve)
from .views import (favourite_list)
from django.http import HttpRequest
from django.contrib.auth.models import User


class FavouriteList(TestCase):
    #test for url profile/favourite
    def test_root_url_resolves_to_favourite_list_view(self):
        found = resolve(reverse('music:favourite_list'))
        self.assertEqual(found.func , favourite_list)

    #checking for file type and title tag
    def test_favourite_list_page_return_correct_html(self):
        request = HttpRequest()
        request.user = User.objects.create()
        response = favourite_list(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!doctype html>'))
        self.assertIn('<title>Favourite Music</title>', html)
