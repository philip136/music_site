from django.test import SimpleTestCase
from django.urls import (reverse,
                         resolve)
from calendarApp.views import CalendarView


class TestUrls(SimpleTestCase):
    def test_calendar_url_is_resolved(self):
        url = reverse('calendar')
        self.assertEqual(resolve(url).func.view_class, CalendarView)


