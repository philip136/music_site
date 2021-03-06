from datetime import (datetime,
                      timedelta)
from calendar import HTMLCalendar
from .models import Calendar


class CalendarUtil(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(CalendarUtil, self).__init__()

    def formatday(self, day, events):
        events_per_day = events.filter(start_event__day=day)
        d = ""
        for event in events_per_day:
            d += f"<li class='title-event' id='title-event'></li>"
        if day !=0:
            return f"<td class='event' id='event-field'><span class='date'>{day}</span><ul> {d} </ul></td>"
        return "<td></td>"

    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'

    def formatmonth(self, withyear=True):
        events = Calendar.objects.filter(start_event__year=self.year, start_event__month=self.month)

        cal = f'<table border="1" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'<hr class="month-line"/>{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal

