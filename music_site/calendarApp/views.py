from django.views.generic import FormView
from .models import Calendar
from datetime import datetime
from django.utils.safestring import mark_safe
from .utils import CalendarUtil
from users.models import Profile
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import EventForm


class CalendarView(FormView):
    model = Calendar
    success_url = reverse_lazy("calendar")
    form_class = EventForm
    template_name = "calendarApp/calendar.html"

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(**kwargs)
        d = get_date(self.request.GET.get("day", None))
        cal = CalendarUtil(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['form'] = form
        return self.render_to_response(context)

    # Validation
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            form.user = Profile.objects.get(user=request.user)
            form.save()
            return redirect(self.success_url)
        context = self.get_context_data(**kwargs)
        context["form"] = form
        return self.render_to_response(context)


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime.date(year, month, day=1)
    return datetime.today()




