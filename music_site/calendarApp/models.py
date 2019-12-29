from django.db import models


#event on calendar
class Calendar(models.Model):
    # celebrate day
    day = models.DateField()
    # begin event
    start_celebrate = models.TimeField()
    # end event
    end_celebrate = models.TimeField()
    # notes (what a event)
    notes = models.TextField(max_length=150)






