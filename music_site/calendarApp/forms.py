from django import forms
from .models import Calendar


class EventForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = ("title", "start_event", "end_event", "notes", "user")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "id": "title"}),
            "start_event": forms.DateTimeInput(attrs={"class": "form-control", "id": "start_event"}),
            "end_event": forms.DateTimeInput(attrs={"class": "form-control", "id": "end_event"}),
            "notes": forms.TextInput(attrs={"class": "form-control", "id": "notes"}),
            "user": forms.HiddenInput(attrs={"class":"form-control", "id": "user"})
        }