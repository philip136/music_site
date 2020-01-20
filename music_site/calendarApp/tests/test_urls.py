from django.test import (SimpleTestCase,
                         TestCase)
from django.urls import (reverse,
                         resolve)
from calendarApp.views import (CalendarView,
                               delete_event,
                               EventUpdate)
from calendarApp.models import Calendar
from django.contrib.auth.models import User
from users.models import Profile
from django.utils import timezone
from datetime import (datetime,
                      timedelta)


class TestUrls(TestCase):
    def test_calendar_url_is_resolved(self):
        url = reverse('calendar')
        self.assertEqual(resolve(url).func.view_class, CalendarView)

    def test_event_delete_url_is_resolved(self):
        user = User.objects.create_user(username="test", password="test1234567")
        event = Calendar.objects.create(
            title="test",
            start_event=datetime.now(tz=timezone.utc),
            end_event=datetime.now(tz=timezone.utc) + timedelta(days=1),
            notes="test",
            user=Profile.objects.get(user=user)
        )
        url = reverse('event-delete', kwargs={"id": event.id})
        self.assertEqual(resolve(url).func, delete_event)

    def test_event_update_url_is_resolved(self):
        user = User.objects.create_user(username="test", password="test1234567")
        event = Calendar.objects.create(
            title="test",
            start_event=datetime.now(tz=timezone.utc),
            end_event=datetime.now(tz=timezone.utc) + timedelta(days=1),
            notes="test",
            user=Profile.objects.get(user=user)
        )
        url = reverse("event-update", kwargs={"pk": event.id})
        self.assertEqual(resolve(url).func.view_class, EventUpdate)


