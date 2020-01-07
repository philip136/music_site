from django.test import (TestCase,
                         Client)
from django.urls import reverse
from calendarApp.models import Calendar



class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.calendar_url = reverse("calendar")

    def test_calendar_GET(self):
        response = self.client.get(self.calendar_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, "calendarApp/calendar.html")