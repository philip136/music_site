from django.db import models
from datetime import (datetime,
                      timedelta)
from users.models import Profile


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


class Event:
    def __init__(self):
        self._day = datetime.now()
        self._finish = datetime.now()+timedelta(days=1)

    @property
    def getStartTimeEvent(self):
        start_event = self._day.replace(hour=0, minute=0, second=0, microsecond=0)
        return start_event

    @getStartTimeEvent.setter
    def getStartTimeEvent(self, day):
        self._day = day

    @property
    def getFinishTimeEvent(self):
        finish_event = self._finish.replace(hour=0, minute=0, second=0, microsecond=0)
        return finish_event

    @getFinishTimeEvent.setter
    def getFinishTimeEvent(self, f_day):
        self._finish = f_day




class Calendar(models.Model):
    title = models.CharField(max_length=150)
    start_event = models.DateTimeField(default=Event().getStartTimeEvent)
    end_event = models.DateTimeField(default=Event().getFinishTimeEvent)
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

    def __str__(self):
        return f'{self.user} - {self.notes_short}'








