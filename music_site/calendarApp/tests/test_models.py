from django.test import TestCase
from calendarApp.models import Calendar
from datetime import (datetime,
                      timedelta)
from users.models import Profile
from django.contrib.auth.models import User
from django.utils import timezone
import random


class TestModels(TestCase):
    @property
    def generate_random_digit(self):
        return f'test' + str(random.randrange(1, 100, 1))

    @property
    def create_profile(self):
        user = User.objects.create_user(self.generate_random_digit, self.generate_random_digit+"@gmail.com",
                                        "1234567test")
        profile = Profile.objects.get(
            user=user
        )
        return profile

    def setUp(self):
        self.calendar = Calendar.objects.create(
            title="test-title",
            start_event=datetime.now(tz=timezone.utc),
            end_event=datetime.now(tz=timezone.utc) + timedelta(days=1),
            notes="test-title it's celebrate",
            user=self.create_profile,
        )

    def tearDown(self):
        self.create_profile.delete()

    def test_title_is_assigned(self):
        self.assertEquals(self.calendar.title, 'test-title')
