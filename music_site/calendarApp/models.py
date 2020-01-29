from django.db import models
from datetime import (datetime,
                      timedelta)
from users.models import (Profile,
                          Friend)


class Calendar(models.Model):
    title = models.CharField(max_length=150)
    start_event = models.DateTimeField()
    end_event = models.DateTimeField()
    notes = models.TextField(max_length=150)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def celebrate_status(self):
        if self.end_event - self.start_event == timedelta(days=1):
            return f"Today,{self.user}celebrate yourself birthday!"
        else:
            return f"Today begin your task and you lost count days!"

    @property
    def notes_short(self):
        if len(self.notes) > 20:
            return f'{self.notes[:20]}...'
        return self.notes

    def __str__(self):
        return f'{self.user} - {self.notes_short}'


""" Создать мэнеджер который будет фильтровать событие которые заканчиваются через 3 дня и меньше,
    ну а после запихнуть дату в div 
"""










