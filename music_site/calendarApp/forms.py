from django import forms
from .models import Calendar
from users.models import Profile


class EventForm(forms.ModelForm):
    profile = forms.HiddenInput(
        attrs={
            "class": "form-control",
            "id": "user",
        }
    )
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

    class Meta:
        model = Calendar
        fields = ("title", "start_event", "end_event", "notes", "user")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "id": "title"}),
            "notes": forms.TextInput(attrs={"class": "form-control", "id": "notes"}),
        }