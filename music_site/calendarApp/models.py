from django.db import models
from datetime import (datetime,
                      timedelta)


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
    def getEvent(self, day):
        self._day = day

    @property
    def getFinishTimeEvent(self):
        finish_event = self._finish.replace(hour=0, minute=0, second=0, microsecond=0)
        return finish_event

    @getFinishTimeEvent.setter
    def getFinishTimeEvent(self, f_day):
        self._finish = f_day



class Calendar(models.Model):
    day = models.DateTimeField()
    start_event = models.TimeField(default=Event().getStartTimeEvent)
    end_event = models.TimeField(default=Event().getFinishTimeEvent)
    notes = models.TextField(max_length=150)






