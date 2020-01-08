from rest_framework import serializers
from calendarApp.models import Calendar



class CalendarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = ('id', 'title', 'start_event', 'end_event', 'notes', 'user')


class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = ('title', 'start_event', 'end_event', 'notes', 'user')


class CalendarUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = ('title', 'start_event', 'end_event', 'notes')


class CalendarDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = ('title', 'start_event', 'end_event', 'notes', 'user')