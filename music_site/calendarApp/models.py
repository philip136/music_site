from django.db import models
from datetime import (datetime,
                      timedelta)
from users.models import Profile
from django.shortcuts import reverse


class WeekDays(models.Model):
    MO = 'MO'
    TU = 'TU'
    WE = 'WE'
    TH = 'TH'
    FR = 'FR'
    SA = 'SA'
    SU = 'SU'
    weekdays = (
        (MO, 'Monday'),
        (TU, 'Tuesday'),
        (WE, 'Wednesday'),
        (TH, 'Thursday'),
        (FR, 'Friday'),
        (SA, 'Saturday'),
        (SU, 'Sunday'),
    )
    name = models.CharField(primary_key=True, choices=weekdays, max_length=10)


class Calendar(models.Model):
    title = models.CharField(max_length=150)
    start_event = models.DateTimeField()
    end_event = models.DateTimeField()
    notes = models.TextField(max_length=150)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def celebrate_status(self):
        if self.end_event - self.start_event == timedelta(days=1):
            return f"Today,{self.user}celebrate yourself birthday!"
        else:
            return f"Today begin your task and you lost count days!"

    @property
    def notes_short(self):
        if len(self.notes) > 20:
            return f'{self.notes[:20]}...'
        return self.notes

    # setter for initial new date
    def __setattr__(self, key, value):
        super(Calendar, self).__setattr__(key, value)
        self.__dict__[key] = value

    def __str__(self):
        return f'{self.user} - {self.notes_short}'








