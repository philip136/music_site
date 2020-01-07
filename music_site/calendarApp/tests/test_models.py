from django.test import TestCase
from calendarApp.models import Calendar
from datetime import (datetime,
                      timedelta)
from users.models import Profile
from django.contrib.auth.models import User




class TestModels(TestCase):
    @property
    def create_profile(self):
        user = User.objects.create_user("test", "test@gmail.com", "1234567test",)
        profile = Profile.objects.create(
            user=user,
            about_me="hello my name is test",
            avatar="default.png"
        )
        return profile


    def setUp(self):
        self.calendar = Calendar.objects.create(
            title="test-title",
            start_event=datetime.now(),
            end_event=datetime.now() + timedelta(days=1),
            notes="test-title it's celebrate",
            user=self.create_profile,
        )

    def test_title_is_assigned(self):
        self.assertEquals(self.calendar.title, 'test-title')