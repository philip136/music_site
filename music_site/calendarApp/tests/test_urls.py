from django.test import SimpleTestCase
from django.urls import (reverse,
                         resolve)
from calendarApp.views import CalendarView
from calendarApp.calendarApi.views_api import  (CalendarViewApi,
                                    CalendarListApi,
                                    CalendarUpdateEventApi,
                                    CalendarDeleteEventApi
                                   )



class TestUrls(SimpleTestCase):
    def test_calendar_url_is_resolved(self):
        url = reverse('calendar')
        self.assertEqual(resolve(url).func.view_class, CalendarView)

    def test_list_url_calendar_api_resolved(self):
        url = reverse('calendar-api')
        self.assertEqual(resolve(url).func.view_class, CalendarListApi)

    def test_create_url_calendar_api_resolved(self):
        url = reverse('calendar-api-create')
        self.assertEqual(resolve(url).func.view_class, CalendarViewApi)

    def test_update_url_calendar_api_resolved(self):
        url = reverse('calendar-api-update', args=[1])
        self.assertEqual(resolve(url).func.view_class, CalendarUpdateEventApi)

    def test_destroy_url_calendar_api_resolved(self):
        url = reverse('calendar-api-delete', args=[1])
        self.assertEqual(resolve(url).func.view_class, CalendarDeleteEventApi)

