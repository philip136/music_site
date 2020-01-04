from django.contrib import admin
from .models import (Calendar,
                     WeekDays)

# Register your models here.
admin.site.register(Calendar)
admin.site.register(WeekDays)