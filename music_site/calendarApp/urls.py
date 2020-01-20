from django.urls import path
from .views import (CalendarView,
                    delete_event,
                    EventUpdate
                    )

urlpatterns = [
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('calendar/event-delete/<int:id>', delete_event, name='event-delete'),
    path('calendar/event-update/<int:pk>/', EventUpdate.as_view(), name='event-update'),
]