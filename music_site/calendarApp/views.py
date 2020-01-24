from django.views.generic import FormView
from .models import Calendar
from datetime import datetime
from django.utils.safestring import mark_safe
from .utils import CalendarUtil
from users.models import Profile
from django.urls import reverse_lazy
from .forms import (EventForm,
                    EventFormUpdate)
from django.http import (HttpResponseRedirect,
                         JsonResponse)
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework import serializers
from django.shortcuts import (get_object_or_404,
                              render)
from django.views.generic import UpdateView
import json


days_of_the_week = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = "__all__"


class CalendarView(FormView):
    model = Calendar
    form_class = EventForm
    template_name = "calendarApp/calendar.html"
    form_error = False

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)

    def get_initial(self):
        initial = super(CalendarView, self).get_initial()
        if self.request.user.is_authenticated:
            initial.update({"user": Profile.objects.get(user=User.objects.get(pk=self.request.user.id))})
        return initial

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(**kwargs)
        if form.is_valid():
            form.save()
            return self.form_valid(form, **kwargs)
        else:
            self.form_error = True
            context["form_error"] = self.form_error
            return self.render_to_response(context)

    def form_valid(self, form):
        response_data = super(CalendarView, self).form_valid(form)
        if self.request.is_ajax():
            title = self.request.POST.get("title")
            start_event = self.request.POST.get("start_event")
            end_event = self.request.POST.get("end_event")
            notes = self.request.POST.get("notes")
            event = Calendar(title=title,
                             start_event=start_event,
                             end_event=end_event,
                             notes=notes,
                             user=Profile.objects.get(user=User.objects.get(id=self.get_initial().get("user"))))
            event.save()
            response_data["title"] = event.title
            response_data["start_event"] = event.start_event
            response_data["end_event"] = event.end_event
            response_data["notes"] = event.notes
            response_data["user"] = event.user
            return JsonResponse(response_data)
        else:
            return response_data

    def get_success_url(self):
        return reverse_lazy("music:home")

    def get_context_data(self, **kwargs):
        context = super(CalendarView, self).get_context_data(**kwargs)
        d = get_date(self.request.GET.get("day", None))
        cal = CalendarUtil(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        number_day = datetime.weekday(datetime.today())
        context['calendar'] = mark_safe(html_cal)
        context["name_day"] = days_of_the_week.get(number_day)
        context["events"] = self.model.objects.filter(user=Profile.objects.get(user=User.objects.get(id=self.request.user.id)))
        context["today"] = datetime.today().day
        return context


class EventUpdate(UpdateView):
    model = Calendar
    form_class = EventFormUpdate
    success_url = reverse_lazy("music:home")
    template_name = "calendarApp/calendar.html"

    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk")
        self.object = get_object_or_404(Calendar, pk=pk)
        return super(EventUpdate, self).get_object(queryset)

    def post(self, request, *args, **kwargs):
        print("q  w e r t y")
        event = self.model.objects.get(pk=self.get_object().pk)
        event.user = Profile.objects.get(user=request.user)
        form = self.form_class(self.request.POST, instance=event)
        print(form.errors)
        if form.is_valid():
            print("form is valid")
            form.save()
            return HttpResponseRedirect(self.success_url)
        context = super(EventUpdate, self).get_context_data(**kwargs)
        context["form"] = form
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(EventUpdate, self).get_context_data(**kwargs)
        d = get_date(self.request.GET.get("day", None))
        cal = CalendarUtil(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        number_day = datetime.weekday(datetime.today())
        context['calendar'] = mark_safe(html_cal)
        context["name_day"] = days_of_the_week.get(number_day)
        context["events"] = self.model.objects.filter(
            user=Profile.objects.get(user=User.objects.get(id=self.request.user.id)))
        context["today"] = datetime.today().day
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime.date(year, month, day=1)
    return datetime.today()


def delete_event(request, id=None):
    event = get_object_or_404(Calendar, id=id)
    creator_event = event.user.user.username
    if request.method == "POST" and request.user.is_authenticated and request.user.username == creator_event:
        event.delete()
        messages.success(request, "Event successfully deleted!")
        return HttpResponseRedirect(reverse_lazy("music:home"))
    return HttpResponseRedirect(reverse_lazy("calendar"))


# --------- TEST -------------
from django.views.generic import TemplateView


class TestViewSOCKET(TemplateView):
    template_name = "calendarApp/notification.html"


