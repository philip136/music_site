from django.apps import AppConfig


class CalendarAppConfig(AppConfig):
    name = 'calendarApp'

    def ready(self):
        print("This is ready function --> return signals bellow")
        from .notifications import signals
