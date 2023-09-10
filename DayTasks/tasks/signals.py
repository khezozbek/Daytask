from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task
import datetime
from celery import shared_task


@receiver(post_save, sender=Task)
def schedule_appointment_notification(sender, instance, **kwargs):
    # Check if the appointment is in the future
    if instance.time > datetime.datetime.now():
        # Calculate the delay in seconds until the appointment time
        delay_seconds = (instance.time - datetime.datetime.now()).total_seconds()

        # Schedule the notification task with Celery
        send_notification.apply_async(args=[instance.pk], countdown=delay_seconds)


@shared_task
def send_notification(appointment_id):
    # Get the appointment object using the appointment_id
    try:
        appointment = Task.objects.get(pk=appointment_id)
    except Task.DoesNotExist:
        return

    # Perform the task for this user (e.g., sending a message on the site)
    # Add your task code here
    print(f"Sending message for appointment: {appointment}")
