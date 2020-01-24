from django.contrib import admin
from .models import Calendar

# Register your models here.
@admin.register(Calendar)
class CalendarEventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_event', 'user', 'notes')
    search_fields = ('title', 'user')
    ordering = ('-start_event',)
    fieldsets = (
        ('Required Information',{
            'description': "These fields are required for each event.",
            'fields': (('title', 'notes'), 'start_event',
                       'end_event', 'user',)
        }),
    )