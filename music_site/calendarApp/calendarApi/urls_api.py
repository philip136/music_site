from django.urls import path
from .views_api import (CalendarViewApi,
                        CalendarListApi,
                        CalendarUpdateEventApi,
                        CalendarDeleteEventApi
                        )


urlpatterns = [
    path('calendar/api/create', CalendarViewApi.as_view(), name='calendar-api-create'),
    path('calendar/api', CalendarListApi.as_view(), name='calendar-api'),
    path('calendar/api/delete/<int:event_id>', CalendarDeleteEventApi.as_view(), name='calendar-api-delete'),
    path('calendar/api/update/<int:event_id>', CalendarUpdateEventApi.as_view(), name='calendar-api-update'),

]