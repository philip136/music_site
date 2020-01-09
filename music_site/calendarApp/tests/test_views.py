from django.test import (TestCase,
                         Client)
from django.urls import reverse
from users.models import Profile
from django.contrib.auth.models import User
from calendarApp.models import Calendar
from datetime import (datetime,
                      timedelta)
from rest_framework.authtoken.models import Token
import json
from rest_framework.test import APITestCase



class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.calendar_url = reverse("calendar")

    def test_calendar_GET(self):
        response = self.client.get(self.calendar_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "calendarApp/calendar.html")



class TestCaseCalendarApi(APITestCase):
    def setUp(self):
        self.profile = self.create_account
        self.calendar_api_list = reverse("calendar-api")
        self.calendar_api_create = reverse("calendar-api-create")
        self.calendar_api_update = reverse("calendar-api-update", kwargs={"event_id": 1})
        self.calendar_api_destroy = reverse("calendar-api-delete", kwargs={"event_id": 1})
        self.token = Token.objects.create(user=self.profile)
        self.api_authentication()

    @property
    def create_account(self):
        user = User.objects.create_user("test123456", "test123456@gmail.com",
                                             "1234567test",)
        return user

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_calendar_api_list(self):
        response = self.client.get(self.calendar_api_list)
        self.assertEquals(response.status_code, 200)

    def test_calendar_api_create(self):
        data = {"title": "test1",
                "start_event": datetime.now(),
                "end_event": datetime.now() + timedelta(days=1),
                "notes": "test_notes1",
                "user": (Profile.objects.get(user=self.profile)).id
                }
        response = self.client.post(self.calendar_api_create, data)
        self.assertEquals(response.status_code, 201)

    #need fix
    def test_calendar_api_update(self):
        data = {"title": "test123",
                "notes": "test_notes123",
                }
        response = self.client.put(self.calendar_api_update, data)
        self.assertEquals(response.status_code, 200)
        self.assertEqual(json.loads(response.content),
                 {"title": "test123",
                  "start_event": datetime.now(),
                  "end_event": datetime.now() + timedelta(days=1),
                  "notes": "test_notes123",
                  "user": (Profile.objects.get(user=self.profile)).id
                  })

    #need fix
    def test_calendar_api_delete(self):
        response = self.client.delete(self.calendar_api_destroy)
        self.assertEqual(response.status_code, 200)








