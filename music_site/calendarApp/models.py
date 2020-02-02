from django.db import models
from datetime import (datetime,
                      timedelta)
from users.models import (Profile,
                          Friend)
from django.utils import timezone
from django.db import connection


class CalendarManager(models.Manager):
    """ Return new queryset if event dont end or more days are left until the end of the event """
    def filter_events_date(self, user):
        new_queryset = []
        queryset = self.filter(user=user)
        print(queryset)
        difference_in_time = timedelta(days=1)
        for event in range(len(queryset)):  
            if queryset[event].end_event.date() - datetime.now(tz=timezone.utc).date() >= difference_in_time:
                new_queryset.append(queryset[event])
            else:
                queryset[event].delete()
        return new_queryset


class Calendar(models.Model):
    title = models.CharField(max_length=150)
    start_event = models.DateTimeField()
    end_event = models.DateTimeField()
    notes = models.TextField(max_length=150)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    fin_event = models.BooleanField(default=False)
    objects = CalendarManager()

    @property
    def notes_short(self):
        if len(self.notes) > 20:
            return f'{self.notes[:20]}...'
        return self.notes

    def __str__(self):
        return f'{self.user} - {self.notes_short}'










