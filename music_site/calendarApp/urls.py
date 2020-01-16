from django.urls import path
from .views import (CalendarView,
                    delete_event)


urlpatterns = [
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('calendar/event-delete/<int:id>', delete_event, name='event-delete'),
]