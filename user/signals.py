# from django.contrib.auth.models import User
from .models import CustomUser as User
from user.tasks import send_welcome_email_task
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    """
    Sends a welcome email and logs a message when a new user is created.
    """
    if created:  # Check if a new user is created
        # Send a welcome email
        send_mail(
            subject="Welcome to Our Platform",
            message=f"Hi {instance.first_name} {instance.last_name}, welcome to our platform!",
            from_email="admin@example.com",
            recipient_list=[instance.email],
            fail_silently=False,
        )

        # Log the registration
        logger.info(f"New user created: {instance.first_name} {instance.last_name} ({instance.email})")


@receiver(post_save, sender=User)
def send_welcome_email2(sender, instance, created, **kwargs):
    if created:
        send_welcome_email_task.delay(instance.username, instance.email)
        logger.info(f"New user created: {instance.username} ({instance.email})")
