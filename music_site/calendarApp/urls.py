from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CalendarView


urlpatterns = [
    path('calendar/', CalendarView.as_view(), name='calendar'),
]