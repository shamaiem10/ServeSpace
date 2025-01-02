from celery import shared_task
from .models import EmailQueue, Volunteer
from django.core.mail import send_mail

@shared_task
def send_assigned_task_email():
    # Same logic as before
    email_queue_entries = EmailQueue.objects.filter(email_sent=False)

    for entry in email_queue_entries:
        volunteer = Volunteer.objects.get(id=entry.volunteer_id)

        # Send the email
        subject = 'Hello, You have been assigned a new task!'
        message = f"Dear {volunteer.full_name},\n\nYou have been assigned a new task (Task ID: {entry.task_id}).\n\nRegards,\nYour Organization"
        send_mail(subject, message, 'no-reply@yourorganization.com', [volunteer.email])

        # Mark the entry as processed
        entry.email_sent = True
        entry.save()
