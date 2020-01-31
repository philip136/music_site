from django.db import models
from datetime import (datetime,
                      timedelta)
from users.models import (Profile,
                          Friend)
from django.utils import timezone


class CalendarManager(models.Manager):
    """ Return new queryset if 3 or more days are left until the end of the event """
    def filter_events_date(self):
        new_queryset = []
        queryset = self.get_queryset()
        difference_in_time = timedelta(days=1)
        for event in range(len(queryset)):
            if queryset[event].end_event.date() - datetime.now(tz=timezone.utc).date() >= difference_in_time:
                new_queryset.append(queryset[event])
        return new_queryset


class Calendar(models.Model):
    title = models.CharField(max_length=150)
    start_event = models.DateTimeField()
    end_event = models.DateTimeField()
    notes = models.TextField(max_length=150)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    fin_event = models.BooleanField(default=False)
    objects = CalendarManager()

    """ Getter for fin_event """
    @property
    def setup_finish_event(self):
        return self.fin_event

    """ Setter for fin_event """
    @setup_finish_event.setter
    def setup_finish_event(self, flag=True):
        self.fin_event = flag

    """ If event already passed or end deadline """
    def is_finished(self):
        if self.fin_event == True or self.end_event < datetime.now(tz=timezone.utc):
            event = Calendar.objects.get(pk=self.pk)
            event.delete()

    @property
    def notes_short(self):
        if len(self.notes) > 20:
            return f'{self.notes[:20]}...'
        return self.notes

    def __str__(self):
        return f'{self.user} - {self.notes_short}'










