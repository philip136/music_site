from calendarApp.models import Calendar
from datetime import (datetime,
                      timedelta)
from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


@receiver(post_save, sender=Calendar)
def announce_new_notification(sender, instance, created, **kwargs):
    if created:
        current_time = datetime.now()
        # one or more days
        if instance.end_event.date() - current_time.date() >= timedelta(days=1):
            channel_layer = get_channel_layer()
            days_left = instance.end_event.date() - current_time.date()
            async_to_sync(channel_layer.group_send)(
                "notifications",
                {
                 "type": "calendar.notifications",
                 "event": "New Notification",
                 "username": instance.user.user.username,
                 "time_to_finish": instance.end_event.date(),
                 "message": f"{days_left} days left to complete the event {instance.title}",
                 }
            )
