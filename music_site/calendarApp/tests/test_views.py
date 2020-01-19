from django.test import (TestCase,
                         Client)
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import Profile
from calendarApp.forms import EventForm
from datetime import (datetime,
                      timedelta)
from django.utils import timezone
from calendarApp.models import Calendar


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.calendar_url = reverse("calendar")
        self.password = "test12345678"
        self.username = "test1"
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.user.save()
        self.event = Calendar.objects.create(
            title="test",
            notes="test",
            start_event=datetime.now(tz=timezone.utc),
            end_event=datetime.now(tz=timezone.utc) + timedelta(days=1),
            user=Profile.objects.get(user=self.user)
        )
        self.event.save()
        self.events = [self.event]

    def test_count_events(self):
        count = 1
        event = Calendar.objects.create(
            title="test",
            notes="test",
            start_event=datetime.now(tz=timezone.utc),
            end_event=datetime.now(tz=timezone.utc) + timedelta(days=1),
            user=Profile.objects.get(user=self.user)
        )
        event.save()
        count += 1
        events = Calendar.objects.filter(user=Profile.objects.get(user=self.user))
        self.assertEqual(events.count(), count)

    def test_calendar_GET(self):
        if self.client.login(username=self.username, password=self.password):
            response = self.client.get(self.calendar_url)
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, "calendarApp/calendar.html")
        else:
            print("Login or password incorrect")

    def test_calendar_POST(self):
        if self.client.login(username=self.username, password=self.password):
            form_data = {
                "title": "test666",
                "start_event": datetime.today(),
                "end_event": datetime.now(tz=timezone.utc),
                "notes": "test766",
                "user": Profile.objects.get(user=self.user)
            }
            response = self.client.post(self.calendar_url, form_data)
            self.events.append(response.context["events"][0])
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(self.events), response.context["events"].count() + 1)
        else:
            print("Login or password incorrect")

    def test_calendar_DELETE(self):
        path_to_delete = reverse("event-delete", kwargs={"id": self.event.id})
        if self.client.login(username=self.username, password=self.password):
            response = self.client.post(path_to_delete, follow=True)
            self.assertEqual(response.status_code, 200)










