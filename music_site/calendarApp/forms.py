from django import forms
from .models import Calendar
from django.core.exceptions import ValidationError
import re


class EventForm(forms.ModelForm):

    start_event = forms.DateTimeField(
        input_formats=["%Y-%m-%dT%H:%M"],
        widget=forms.DateTimeInput(
            attrs={
                "type": "datetime-local",
                "class": "form-control",
                "id": "start_event",
            },
            format="%Y-%m-%dT%H:%M"
        )
    )
    end_event = forms.DateTimeField(
        input_formats=["%Y-%m-%dT%H:%M"],
        widget=forms.DateTimeInput(
            attrs={
                "type": "datetime-local",
                "class": "form-control",
                "id": "end_event",
            },
            format="%Y-%m-%dT%H:%M"
        ))

    def clean_end_event(self):
        start_event = self.cleaned_data["start_event"]
        end_event = self.cleaned_data["end_event"]
        if start_event > end_event:
            raise ValidationError("End event date not must be earlier then start event date")
        return end_event

    def clean_title(self):
        title = self.cleaned_data["title"]
        regular = re.search(r"^\D", title)
        if regular == None:
            raise ValidationError("Event title must begin with a letter")
        return title

    class Meta:
        model = Calendar
        fields = ("title", "start_event", "end_event", "notes", "user")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "id": "title"}),
            "notes": forms.TextInput(attrs={"class": "form-control", "id": "notes"}),
            "user": forms.HiddenInput(attrs={"class": "form-control", "id": "user"})
        }


class EventFormUpdate(EventForm):
    class Meta:
        model = Calendar
        fields = ("title", "start_event", "end_event", "notes")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "id": "title"}),
            "notes": forms.TextInput(attrs={"class": "form-control", "id": "notes"}),
        }