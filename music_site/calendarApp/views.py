from django.views.generic import ListView
from .models import Calendar
from datetime import datetime
from django.utils.safestring import mark_safe
from .utils import CalendarUtil
from users.models import Profile
from django.shortcuts import render




class CalendarView(ListView):
    model = Calendar
    template_name = "calendarApp/calendar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get("day", None))
        cal = CalendarUtil(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['user'] = (Profile.objects.get(user=self.request.user)).id
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime.date(year, month, day=1)
    return datetime.today()



